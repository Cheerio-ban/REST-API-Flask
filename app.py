#!/usr/bin/env python3

from flask import Flask, jsonify, abort

app = Flask(__name__)


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


# api format appname/api/version/folder/id
@app.route("/todo/api/v1.0/tasks", methods= ["GET"])
def home():
    return jsonify({'tasks': tasks})

@app.route("/todo/api/v1.0/tasks/<int:task_id>", methods = ["GET"])
def get_user(task_id):
    for task in tasks:
        if task['id'] == task_id:
            return jsonify({'task': task})
    return abort('404')

if __name__ == '__main__':
    app.run(debug=True)
