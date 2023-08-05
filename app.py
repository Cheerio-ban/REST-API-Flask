#!/usr/bin/env python3

from flask import jsonify, abort, make_response, request
from data import todos
from models import Task, db
from config import app
# db = SQLAlchemy(app)

app.app_context().push()
db.create_all()


# Fetches all data from the database
tasks = Task.query.all()

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# api format appname/api/version/folder/id
@app.route("/todo/api/v1.0/tasks", methods= ["GET"])
def home():
    # Used this workaround because SQLalchemy class object can't be jsonified.
    task_list = []
    for task in tasks:
        list_elem = {   'id': task.id,
                        'title': task.title,
                        'description': task.description,
                        'completed': task.completed
                    }
        task_list.append(list_elem)
    return jsonify({'tasks': task_list})

@app.route("/todo/api/v1.0/tasks/<int:task_id>", methods = ["GET"])
def get_task(task_id):
    task = Task.query.filter_by(id=task_id).first()
    if not task:
        abort(404)
    return jsonify({'task': { 'id': task.id,
                             'title': task.title,
                             'description': task.description,
                             'completed': task.completed
                             }})

@app.route("/todo/api/v1.0/tasks", methods= ["POST"])
def create_task():
    if not request.json or 'title' not in request.json:
        abort(400)
    task = Task(title=request.json['title'])
    task.description = request.json.get('description', '')
    task.completed = False

    db.session.add(task)
    db.session.commit()
    return jsonify({'task': { 'id': task.id,
                             'title': task.title,
                             'description': task.description,
                             'completed': task.completed
                             }
                    }), 201


@app.route("/todo/api/v1.0/tasks/<int:task_id>", methods = ["PUT"])
def update_task(task_id):
    if not request.json:
        abort(400)
    task = Task.query.filter_by(id = task_id).first()
    if not task:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400)
    if 'description' in request.json and type(request.json['description']) != str:
        abort(400)
    if 'done' in request.json and type(request.json['done']) != bool:
        abort(400)
    task.title = request.json.get('title', task.title)
    task.description = request.json.get('description', task.description)
    task.completed = request.json.get('done', task.completed)
    db.session.commit()
    return jsonify({'task': { 'id': task.id,
                             'title': task.title,
                             'description': task.description,
                             'completed': task.completed
                             }})



@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.filter_by(id=task_id)
    if not task:
        abort(400)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'result': True})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
