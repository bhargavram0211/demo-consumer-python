"""
Simple Flask API Demo Application
This app intentionally contains secrets for testing Sentinel-Flow secret scanning
"""

from flask import Flask, jsonify
import os

app = Flask(__name__)

# WARNING: These are intentional test secrets for demo purposes
# In a real application, NEVER hardcode credentials!

# AWS Credentials (INTENTIONAL TEST SECRET - will be detected by Gitleaks)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLETEST"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEYTEST"

# GitHub Personal Access Token (INTENTIONAL TEST SECRET)
GITHUB_TOKEN = "ghp_123456789abcdefghijklmnopqrstuvwxyzABCD"

# Database Connection String (INTENTIONAL TEST SECRET)
DATABASE_URL = "postgresql://admin:SuperSecretP@ssw0rd123@localhost:5432/mydb"

# API Key (INTENTIONAL TEST SECRET)
API_KEY = "sk_live_51Hxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        'message': 'Welcome to Demo Consumer API',
        'status': 'running',
        'security': 'This repo uses Sentinel-Flow for secret scanning'
    })


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'version': '1.0.0'
    })


@app.route('/api/data')
def get_data():
    """Sample data endpoint"""
    # In a real app, you'd use environment variables:
    # api_key = os.environ.get('API_KEY')
    
    return jsonify({
        'data': [
            {'id': 1, 'name': 'Sample Item 1'},
            {'id': 2, 'name': 'Sample Item 2'},
            {'id': 3, 'name': 'Sample Item 3'}
        ],
        'count': 3
    })


if __name__ == '__main__':
    # Don't use debug=True in production!
    app.run(debug=True, host='0.0.0.0', port=5000)
