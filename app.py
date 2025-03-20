from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)
@app.route('/api/v1/contact', methods=['POST'])
def create_contact():
    return jsonify({}), 201

@app.route('/api/v1/contact/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def contact(id):
    if request.method == 'GET':
        return jsonify({}), 200
    elif request.method == 'PUT':
        return jsonify({}), 200
    elif request.method == 'DELETE':
        return jsonify({}), 204

@app.route('/api/v1/group', methods=['POST'])
def create_group():
    return jsonify({}), 201

@app.route('/api/v1/group/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def group(id):
    if request.method == 'GET':
        return jsonify({}), 200
    elif request.method == 'PUT':
        return jsonify({}), 200
    elif request.method == 'DELETE':
        return jsonify({}), 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6080)