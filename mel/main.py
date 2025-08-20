#!/usr/bin/env python3
"""
Servidor web simples para o EcoConecta - Site estático
"""
from flask import Flask, send_from_directory, redirect
import os

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory('.', filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)