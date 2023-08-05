#!/usr/bin/env python3

from flask import Flask, jsonify, abort, make_response, request
from data import todos
from models import Task
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

app.app_context().psh()
db.create_all()



for elem in todos:
    task = Task(title=elem['todo'])
    task.completed = elem['completed']
    db.session.add(task)

db.session.commit()
# Harded coded data to simulate data in a database
tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# api format appname/api/version/folder/id
@app.route("/todo/api/v1.0/tasks", methods= ["GET"])
def home():
    return jsonify({'tasks': tasks})

@app.route("/todo/api/v1.0/tasks/<int:task_id>", methods = ["GET"])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task})

@app.route("/todo/api/v1.0/tasks", methods= ["POST"])
def create_task():
    if not request.json or 'title' not in request.json:
        abort(400)
    task = {
            'id': tasks[-1]['id'] + 1,
            'title': request.json['title'],
            'description': request.json.get('description', ''),
            'done': False,
            }
    tasks.append(task)
    return jsonify({'task': task}), 201


@app.route("/todo/api/v1.0/tasks/<int:task_id>", methods = ["PUT"])
def edit_task(task_id):
    if not request.json:
        abort(400)
    task = [task for task in tasks if task["id"] == task_id]
    if len(task) == 0:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400)
    if 'description' in request.json and type(request.json['description']) != str:
        abort(400)
    if 'done' in request.json and type(request.json['done']) != bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})



@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
