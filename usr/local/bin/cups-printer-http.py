from flask import Flask, request, jsonify
from datetime import datetime
import subprocess
import os
import re

app = Flask(__name__)

@app.route('/print', methods=['POST'])
def print_document():
    if 'file' not in request.files:
        return jsonify({
            "status": 400,
            "error": "Bad Request",
            "message": "Field 'file' is required."
        }), 400

    if 'printer' not in request.form:
        return jsonify({
            "status": 400,
            "error": "Bad Request",
            "message": "Field 'printer' is required."
        }), 400
    
    file = request.files['file']
    printer_name = request.form['printer']
    
    job = request.form.get('job', None)
    server = request.form.get('server', '127.0.0.1')
    
    file_location = f"/tmp/{file.filename}"
    file.save(file_location)
    
    lp_command = ["lp", "-h", server, "-d", printer_name, file_location]
    if job:
        lp_command += ["-t", job]

    try:
        result = subprocess.run(lp_command, check=True, capture_output=True, text=True, timeout=10)
        pattern = r'request id is ([A-Za-z0-9\-]+)'
        match = re.search(pattern, result.stdout)
        request_id = match.group(1)
        
        return jsonify({
            "status": 200,
            "error": False,
            "message": "Print request processed successfully.",
            "request_id": request_id
        }), 200

    except Exception as e:

        return jsonify({
            "status": 500,
            "error": str(e),
            "message": "An error occurred while processing the print job."
        }), 500
    
    finally:
        
        try:
            os.remove(file_location)
        except OSError:
            pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=632)
