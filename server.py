#!/usr/bin/env python3
"""
Combined Server for FreeFire API and Web Interface
This script serves both the API endpoints and the web frontend.
"""

import os
import sys
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the existing app
try:
    from app import app as api_app
except ImportError as e:
    print(f"Error importing app: {e}")
    sys.exit(1)

# Create a new Flask app that combines both
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Register the API routes
# Serve static files (HTML, CSS, JS)
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    # Serve static files from the current directory
    if os.path.exists(os.path.join('.', path)):
        return send_from_directory('.', path)
    else:
        # Return 404 for non-existent files
        return "File not found", 404

# Health check endpoint
@app.route('/health')
def health_check():
    return jsonify({"status": "healthy", "service": "FreeFire-API-Manager"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"[🚀] Starting FreeFire API Manager on port {port} ...")
    app.run(host='0.0.0.0', port=port, debug=False)