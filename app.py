from flask import Flask,redirect, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

class Task(db.Model):
    # __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(200), nullable=False)
    status = db.Column(db.Boolean, default=False)
    
with app.app_context():
    db.create_all()

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = Task(task_name=data['task_name'])
    print("Tasks from database:", new_task) 
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task added successfully', 'task': {
        'id': new_task.id,
        'task_name': new_task.task_name,
        'status': new_task.status
    }}), 201
    
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{'id': task.id, 'task_name': task.task_name, 'status': task.status} for task in tasks]), 200

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    task.status = data.get('status', task.status)
    task.task_name = data.get('task_name', task.task_name)
    db.session.commit()
    return jsonify({'message': 'Task updated successfully', 'task': {
        'id': task.id,
        'task_name': task.task_name,
        'status': task.status
    }}), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully'}), 200


@app.route("/")
def hello_world():
    return "Hello, World!"



