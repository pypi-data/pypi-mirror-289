from flask import Flask, request, jsonify, send_from_directory, Response, render_template
from werkzeug.utils import safe_join
from flask_cors import CORS
from papertlab.main import main as cli_main
from papertlab.coders import Coder
from papertlab import models
import os
import json
from pathlib import Path
import traceback
import sys
from io import StringIO
import threading
import sqlite3
from datetime import datetime, date
import subprocess
from papertlab.io import InputOutput

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Add a global variable to store the current model
current_model = None

def execute_command(cmd):
    """
    Executes a command in the command line and returns the output and error messages.

    Parameters:
    cmd (str): The command to execute.

    Returns:
    tuple: A tuple containing the command's standard output and standard error.
    """
    try:
        result = subprocess.run(cmd, shell=True, check=True, text=True, capture_output=True)
        return result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        return e.stdout, e.stderr

def get_available_models():
    models = []
    if 'ANTHROPIC_API_KEY' in os.environ:
        models.extend([
            "claude-3-5-sonnet-20240620",
            "claude-3-opus-20240229",
            "claude-3-haiku-20240307",
        ])
    if 'OPENAI_API_KEY' in os.environ:
        models.extend([
            "gpt-4o",
            "gpt-4-0613",
            "gpt-4-turbo-preview",
            "gpt-4-1106-preview",
            "gpt-3.5-turbo",
        ])
    return models

DEFAULT_MODEL = "claude-3-5-sonnet-20240620" if 'ANTHROPIC_API_KEY' in os.environ else "gpt-4o"
coder = None
coder_lock = threading.Lock()
DB_PATH = 'papertlab_gui.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS project_usage (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id TEXT,
            model TEXT,
            input_token INTEGER,
            output_token INTEGER,
            cost REAL,
            total_cost REAL,
            datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Check if all required columns exist, if not, add them
    cursor.execute("PRAGMA table_info(project_usage)")
    columns = [column[1] for column in cursor.fetchall()]
    required_columns = ['project_id','model', 'input_token', 'output_token', 'cost', 'total_cost', 'datetime']
    for column in required_columns:
        if column not in columns:
            cursor.execute(f'ALTER TABLE project_usage ADD COLUMN {column}')
            if column == 'datetime':
                cursor.execute(f'UPDATE project_usage SET {column} = CURRENT_TIMESTAMP WHERE {column} IS NULL')
    
    conn.commit()
    conn.close()

init_db()

class Logger:
    def __init__(self):
        self.logs = []
        self.capture = False
        self.lock = threading.Lock()

    def write(self, message):
        with self.lock:
            if "POST /api/chat HTTP/1.1" in message:
                self.capture = True
            if self.capture:
                self.logs.append(message.strip())
            sys.__stdout__.write(message)  # Use sys.__stdout__ to avoid recursion

    def flush(self):
        sys.__stdout__.flush()

    def get_logs(self):
        with self.lock:
            logs = self.logs
            self.logs = []
            self.capture = False
            return logs

logger = Logger()
sys.stdout = logger
sys.stderr = logger

print("papertlab GUI started. Initializing...")

def handle_recursion_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except RecursionError:
            error_message = "RecursionError: maximum recursion depth exceeded"
            print(error_message, file=sys.__stderr__)
            return jsonify({"error": error_message}), 500
    return wrapper

# API endpoint to get the current API keys
@app.route('/api/get_api_keys', methods=['GET'])
def get_api_keys():
    openai_api_key = os.getenv('OPENAI_API_KEY', '')
    anthropic_api_key = os.getenv('ANTHROPIC_API_KEY', '')
    return jsonify({
        'openai_api_key': openai_api_key,
        'anthropic_api_key': anthropic_api_key
    })

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return send_from_directory(app.template_folder, 'index.html')

@app.route('/usage')
def serve_usage():
    return send_from_directory(app.template_folder, 'usage.html')

@app.route('/static/usage.js')
def serve_usage_js():
    return send_from_directory(app.template_folder, 'usage.js')

@app.route('/settings')
def serve_settings():
    return render_template('settings.html')

@app.route('/static/history.html')
def serve_history():
    return send_from_directory(app.template_folder, 'history.html')

@app.route('/api/check_api_key', methods=['GET'])
def check_api_key():
    openai_key_present = 'OPENAI_API_KEY' in os.environ
    anthropic_key_present = 'ANTHROPIC_API_KEY' in os.environ

    if openai_key_present or anthropic_key_present:
        return jsonify({
            "openai_key_present": openai_key_present,
            "anthropic_key_present": anthropic_key_present
        })
    else:
        return jsonify({
            "openai_key_present": False,
            "anthropic_key_present": False
        })

    
def get_uncommitted_files():
    try:
        # Get list of untracked files
        untracked_files = subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard']).decode().splitlines()
        
        # Get list of modified files
        modified_files = subprocess.check_output(['git', 'diff', '--name-only']).decode().splitlines()
        
        # Get list of staged files
        staged_files = subprocess.check_output(['git', 'diff', '--staged', '--name-only']).decode().splitlines()
        
        uncommitted_files = list(set(untracked_files + modified_files + staged_files))
        
        if uncommitted_files:
            print(f"Uncommitted files found: {uncommitted_files}")
        else:
            print("No uncommitted files found.")
        
        return uncommitted_files
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while checking for uncommitted files: {e}")
        return []

@handle_recursion_error
@app.route('/api/init', methods=['POST'])
def initialize():
    global coder, current_model
    with coder_lock:
        if coder is None:
            print("Initializing Coder...")
            try:
                # Get uncommitted files before initializing
                uncommitted_files = get_uncommitted_files()
                print("uncommitted_files==================", uncommitted_files)

                coder = cli_main(return_coder=True)

                if uncommitted_files and uncommitted_files != []:
                    coder.auto_commit(set(uncommitted_files))

                if not isinstance(coder, Coder):
                    raise ValueError("Failed to initialize Coder")
                coder.main_model = models.Model(DEFAULT_MODEL)
                print("Coder initialized successfully")
            except Exception as e:
                print(f"Error initializing Coder: {str(e)}")
                return jsonify({"error": f"Failed to initialize Coder: {str(e)}"}), 500
            
    if current_model is None:
        current_model = DEFAULT_MODEL  # Set this to your default model

    return jsonify({
        "announcements": coder.get_announcements(),
        "files": get_file_structure(coder.get_all_relative_files()),
        "initial_chat_files": coder.get_inchat_relative_files(),
        "models": get_available_models(),
        "current_model": current_model
    })

@handle_recursion_error
@app.route('/api/usage', methods=['GET'])
def get_usage():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    offset = (page - 1) * per_page

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Get total count
    cursor.execute('SELECT COUNT(*) FROM project_usage')
    total_count = cursor.fetchone()[0]
    
    # Get paginated data
    cursor.execute('''
        SELECT id, project_id, model, input_token, output_token, cost, total_cost, datetime
        FROM project_usage
        ORDER BY datetime DESC
        LIMIT ? OFFSET ?
    ''', (per_page, offset))
    
    results = cursor.fetchall()
    conn.close()
    
    usage_data = [
        {
            "id": row[0],
            "project_id": row[1],
            "model": row[2],
            "input_token": row[3],
            "output_token": row[4],
            "cost": row[5],
            "total_cost": row[6],
            "datetime": row[7]
        }
        for row in results
    ]
    
    return jsonify({
        "usage": usage_data,
        "total": total_count
    })

@app.route('/api/monthly_usage', methods=['GET'])
def get_monthly_usage():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Get the first day of the current month
        first_day_of_month = date.today().replace(day=1).isoformat()
        
        # Get total tokens and cost for the current month
        cursor.execute('''
            SELECT SUM(input_token + output_token) as total_tokens, SUM(cost) as total_cost
            FROM project_usage
            WHERE datetime >= ?
        ''', (first_day_of_month,))
        
        result = cursor.fetchone()
        conn.close()
        
        total_tokens = int(result[0] or 0)
        total_cost = float(result[1] or 0)
        
        return jsonify({
            "total_tokens": total_tokens,
            "total_cost": total_cost
        })
    except Exception as e:
        print(f"Error in get_monthly_usage: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/api/set_model', methods=['PUT'])
def set_model():
    global coder, current_model
    data = request.json
    new_model = data.get('model')
    
    if not new_model:
        return jsonify({"error": "No model specified"}), 400

    with coder_lock:
        if coder is None:
            return jsonify({"error": "Coder not initialized"}), 500

        try:
            # Create a new coder instance with the new model
            new_coder = cli_main(return_coder=True)
            new_coder.main_model = models.Model(new_model)
            
            # Copy over relevant state from the old coder
            new_coder.abs_fnames = coder.abs_fnames
            new_coder.cur_messages = coder.cur_messages
            new_coder.done_messages = coder.done_messages
            
            # Replace the old coder with the new one
            coder = new_coder

            current_model = new_model  
            
            # Get updated announcements and files
            announcements = coder.get_announcements()
            files = get_file_structure(coder.get_all_relative_files())
            
            return jsonify({
                "success": True,
                "message": f"Model set to {new_model}",
                "current_model": current_model,
                "announcements": announcements,
                "files": files or {}  # Ensure files is always an object
            })
        except Exception as e:
            return jsonify({"error": f"Failed to set model: {str(e)}"}), 500
        
def get_latest_usage():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT SUM(input_token + output_token) as total_tokens, SUM(cost) as total_cost
        FROM project_usage
    ''')
    result = cursor.fetchone()
    conn.close()
    return {
        'total_tokens': result[0] or 0,
        'total_cost': result[1] or 0
    }

@app.route('/api/chat', methods=['POST'])
def chat():
    global coder, logger
    data = request.json
 
    with coder_lock:
        if coder is None:
            print("Error: Coder not initialized")
            return jsonify({"error": "Coder not initialized"}), 500

    model = data.get('model', DEFAULT_MODEL)
    print(f"Received chat message: {data['message']} (model: {model})")

    def generate():
        try:
            total_tokens = 0
            yield f"data: {json.dumps({'chunk': 'Analysing the code\n'})}\n\n"

            coder.run(data['message'])

            # print(coder.partial_response_content)
            messages = coder.partial_response_content # dict(coder.get_chat_history()[-1])
            
            # Update project usage in the database
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            # Get the project name from the current working directory
            project_name = os.path.basename(os.getcwd())
            cursor.execute('''
                INSERT INTO project_usage (project_id, model, input_token, output_token, cost, total_cost, datetime)
                VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            ''', (project_name, model, coder.input_token, coder.output_token, coder.cost, coder.total_cost))
            conn.commit()
            conn.close()

            # Log message
            yield f"data: {json.dumps({'chunk': f"{messages}\n"})}\n\n"

            # Get and send updated usage information
            latest_usage = get_latest_usage()
            yield f"data: {json.dumps({'usage': latest_usage})}\n\n"

            # Send completion message
            completion_message = f"Task completed.\n"
            yield f"data: {json.dumps({'chunk': completion_message})}\n\n"

            # After the chat completion, automatically apply changes
            coder.apply_updates()
            yield f"data: {json.dumps({'chunk': 'Changes applied automatically\n'})}\n\n"

            # Update file structure after changes
            updated_files = get_file_structure(coder.get_all_relative_files())
            yield f"data: {json.dumps({'updated_files': updated_files})}\n\n"

            if coder.git_commit_id and coder.git_commit_id != '':
                commit_id = '\n\n' + coder.git_commit_id + '\n\n'
                yield f"data: {json.dumps({'chunk': commit_id})}\n\n"

            # Update file structure after changes
            usage_report = coder.usage_report
            yield f"data: {json.dumps({'chunk': usage_report})}\n\n"

        except Exception as e:
            error_message = f"An error occurred: {str(e)}\n{traceback.format_exc()}"
            print(f"Error: {error_message}")
            yield f"data: {json.dumps({'error': error_message, 'logs': logger.get_logs()})}\n\n"

    return Response(generate(), mimetype='text/event-stream')

@app.route('/api/execute_command', methods=['POST'])
def execute_command_route():
    global coder
    data = request.json
    command = data['command']
    
    if not coder:
        return jsonify({"error": "Coder not initialized"}), 500

    stdout, stderr = execute_command(command)
    
    if stdout:
        result = stdout.strip()
    elif stderr:
        result = f"Error: {stderr.strip()}"
    else:
        result = "Command executed successfully, but returned no output."
    
    return jsonify({"result": result})

@app.route('/api/logs', methods=['GET'])
def get_logs():
    global logger
    logs = logger.get_logs()
    return jsonify({"logs": logs})

@app.route('/api/file_content', methods=['GET'])
def get_file_content():
    global coder
    file_path = request.args.get('file')
    if not file_path:
        return jsonify({"error": "No file specified"}), 400

    try:
        # Use the current working directory as the root
        root_dir = os.getcwd()
        
        # Handle the special case for papertlab files
        if file_path.startswith('papertlab/') or file_path.startswith('papertlab\\'):
            root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # Normalize the file path
        file_path = file_path.replace('\\', '/')
        
        # Use safe_join to prevent path traversal attacks
        safe_path = safe_join(root_dir, file_path)
        
        if safe_path is None or not os.path.exists(safe_path):
            return jsonify({"error": f"File not found: {file_path}"}), 404

        if os.path.getsize(safe_path) == 0:
            return jsonify({"content": ""})

        with open(safe_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return jsonify({"content": content})
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return jsonify({"error": f"Error reading file: {str(e)}"}), 500

@app.route('/api/update_file', methods=['POST'])
def update_file():
    global coder
    data = request.json
    file_path = data.get('file')
    new_content = data.get('content')

    if not file_path or new_content is None:
        return jsonify({"error": "File path and content are required"}), 400

    try:
        # Use the current working directory as the root
        root_dir = os.getcwd()
        
        # Handle the special case for papertlab files
        if file_path.startswith('papertlab/') or file_path.startswith('papertlab\\'):
            root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # Normalize the file path
        file_path = file_path.replace('\\', '/')
        
        # Use safe_join to prevent path traversal attacks
        safe_path = safe_join(root_dir, file_path)
        
        if safe_path is None or not os.path.exists(safe_path):
            return jsonify({"error": f"File not found: {file_path}"}), 404

        # Use the InputOutput class to write the file
        io = InputOutput()
        io.write_text(safe_path, new_content)

        return jsonify({"message": f"File {file_path} updated successfully"})
    except Exception as e:
        print(f"Error updating file: {str(e)}")
        return jsonify({"error": f"Error updating file: {str(e)}"}), 500

@app.route('/api/set_api_key', methods=['POST'])
def set_api_key():
    data = request.json
    openai_key = data.get('openai_key')
    anthropic_key = data.get('anthropic_key')

    if openai_key and openai_key != '':
        os.environ['OPENAI_API_KEY'] = openai_key
    if anthropic_key and anthropic_key != '':
        os.environ['ANTHROPIC_API_KEY'] = anthropic_key
    
    return jsonify({"success": True})

def get_file_structure(files):
    file_structure = {}
    for file in files:
        parts = Path(file).parts
        current = file_structure
        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            current = current[part]
        current[parts[-1]] = file
    return file_structure

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, threaded=True)
