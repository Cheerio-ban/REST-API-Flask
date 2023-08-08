#!/usr/bin/env python3

from flask import jsonify, abort, make_response, request
from data import quotes
from models import Task, Quote, User, Post, db
from config import app
# db = SQLAlchemy(app)

app.app_context().push()
db.create_all()


# Fetches all data from the database
tasks = Task.query.all()
quotes = Quote.query.all()
users = User.query.all()
posts = Post.query.all()


# todos
# api format appname/api/version/folder/id
@app.route("/todo/api/v1.0/tasks", methods=["GET"])
def tasks_index():
    # Used this workaround because SQLalchemy class object can't be jsonified.
    task_list = []
    for task in tasks:
        list_elem = {'id': task.id,
                     'title': task.title,
                     'description': task.description,
                     'completed': task.completed
                     }
        task_list.append(list_elem)
    return jsonify({'tasks': task_list})


@app.route("/todo/api/v1.0/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    """
    Gets a particular task from the Task table in database.
    """
    task = Task.query.filter_by(id=task_id).first()
    if not task:
        abort(404)
    return jsonify({'task': {'id': task.id,
                             'title': task.title,
                             'description': task.description,
                             'completed': task.completed
                             }})


@app.route("/todo/api/v1.0/tasks", methods=["POST"])
def create_task():
    if not request.json or 'title' not in request.json:
        abort(400)
    task = Task(title=request.json['title'])
    task.description = request.json.get('description', '')
    task.completed = False

    db.session.add(task)
    db.session.commit()
    return jsonify({'task': {'id': task.id,
                             'title': task.title,
                             'description': task.description,
                             'completed': task.completed
                             }
                    }), 201


@app.route("/todo/api/v1.0/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    """
    Updates task with task_id.
    """
    if not request.json:
        abort(400)
    task = Task.query.filter_by(id=task_id).first()
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
    return jsonify({'task': {'id': task.id,
                             'title': task.title,
                             'description': task.description,
                             'completed': task.completed
                             }})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """ Deletes task with task_id from the database. """
    task = Task.query.filter_by(id=task_id)
    if not task:
        abort(400)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'result': True})


# quotes
# api structure appname/api/version/folder/id
@app.route("/motive/api/v1.0/quotes", methods=["GET"])
def quotes_index():
    """
    Gets all quotes from the Quote table in database.
    """
    quote_list = []
    for quote in quotes:
        list_elem = {'id': quote.id,
                     'quote': quote.quote,
                     'author': quote.author,
                     }
        quote_list.append(list_elem)
    return jsonify({'quotes': quote_list})


@app.route("/motive/api/v1.0/quotes/<int:quote_id>", methods=["GET"])
def get_quote(quote_id):
    """
    Gets a particular quote from the Quote database.
    """
    quote = Quote.query.filter_by(id=quote_id).first()
    if not quote:
        abort(404)
    return jsonify({'quote': {'id': quote.id,
                              'quote': quote.quote,
                              'author': quote.author,
                              }})


@app.route("/motive/api/v1.0/quotes", methods=["POST"])
def create_quote():
    """
    Creates a new quote in the quotes database
    """
    if not request.json or 'quote' not in request.json:
        abort(400)
    quote = Quote(quote=request.json['quote'])
    quote.author = request.json.get('author', '')

    db.session.add(quote)
    db.session.commit()
    return jsonify({'quote': {'id': quote.id,
                              'quote': quote.quote,
                              'author': quote.author,
                              }
                    }), 201


@app.route("/motive/api/v1.0/quotes/<int:quote_id>", methods=["PUT"])
def update_quote(quote_id):
    """
    Updates quote with quote_id
    """
    if not request.json:
        abort(400)
    quote = Quote.query.filter_by(id=quote_id).first()
    if not quote:
        abort(400)
    if 'quote' in request.json and type(request.json['quote']) != str:
        abort(400)
    if 'author' in request.json and type(request.json['author']) != str:
        abort(400)
    quote.quote = request.json.get('quote', quote.quote)
    quote.author = request.json.get('author', quote.author)
    db.session.commit()
    return jsonify({'quote': {'id': quote.id,
                              'quote': quote.quote,
                              'author': quote.author,
                              }})


@app.route('/motive/api/v1.0/quotes/<int:quote_id>', methods=['DELETE'])
def delete_quote(quote_id):
    """ Deletes quote with quote_id from the database. """
    quote = Quote.query.filter_by(id=quote_id)
    if not quote:
        abort(400)
    db.session.delete(quote)
    db.session.commit()
    return jsonify({'result': True})


# users -> Social appname
# api format appname/api/version/folder/id
@app.route("/social/api/v1.0/users", methods=["GET"])
def users_index():
    """
    Gets all users from the User table in database.
    """
    user_list = []
    for user in users:
        list_elem = {'id': user.id,
                     'firstName': user.firstName,
                     'lastName': user.lastName,
                     'maidenName': user.maidenName,
                     'age': user.age,
                     "gender": user.gender,
                     "email": user.email,
                     "phone": user.phone,
                     "username": user.username,
                     "password": user.password,
                     "university": user.university
                     }
        user_list.append(list_elem)
    return jsonify({'users': user_list})


@app.route("/social/api/v1.0/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    """
    Gets a particular user from the User table in database.
    """
    user = User.query.filter_by(id=user_id).first()
    if not user:
        abort(404)
    return jsonify({'user': {'id': user.id,
                             'firstName': user.firstName,
                             'lastName': user.lastName,
                             'maidenName': user.maidenName,
                             'age': user.age,
                             "gender": user.gender,
                             "email": user.email,
                             "phone": user.phone,
                             "username": user.username,
                             "password": user.password,
                             "university": user.university
                             }})


@app.route("/social/api/v1.0/users", methods=["POST"])
def create_user():
    """
    Creates a new user in the User table in database
    """
    if not request.json or 'username' not in request.json:
        abort(400)
    user = User(username=request.json['username'])
    user.firstName = request.json.get('firstName')
    user.lastName = request.json.get('lastName')
    user.maidenName = request.json.get('maidenName', '')
    user.age = request.json.get('age', '')
    user.gender = request.json.get('gender', '')
    user.email = request.json.get('email', '')
    user.phone = request.json.get('phone', '')
    user.password = request.json.get('password', '')
    user.university = request.json.get('university', '')

    db.session.add(user)
    db.session.commit()
    return jsonify({'user': {'id': user.id,
                             'firstName': user.firstName,
                             'lastName': user.lastName,
                             'maidenName': user.maidenName,
                             'age': user.age,
                             "gender": user.gender,
                             "email": user.email,
                             "phone": user.phone,
                             "username": user.username,
                             "password": user.password,
                             "university": user.university
                             }
                    }), 201


@app.route("/social/api/v1.0/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    """
    Updates user with user_id in User table database.
    """
    if not request.json:
        abort(400)
    user = User.query.filter_by(id=user_id).first()
    if not user:
        abort(400)
    if 'username' in request.json and type(request.json['username']) != str:
        abort(400)
    if 'firstName' in request.json and type(request.json['firstName']) != str:
        abort(400)
    if 'lastName' in request.json and type(request.json['lastName']) != bool:
        abort(400)
    user.username = request.json.get('username', user.username)
    user.firstName = request.json.get('firstName', user.firtName)
    user.lastName = request.json.get('lastName', user.lastName)
    user.maidenName = request.json.get('maidenName', user.maidenName)
    user.age = request.json.get('age', user.age)
    user.gender = request.json.get('gender', user.gender)
    user.email = request.json.get('email', user.email)
    user.phone = request.json.get('phone', user.phone)
    user.password = request.json.get('password', user.password)
    user.university = request.json.get('university', user.university)

    db.session.commit()
    return jsonify({'user': {'id': user.id,
                             'firstName': user.firstName,
                             'lastName': user.lastName,
                             'maidenName': user.maidenName,
                             'age': user.age,
                             "gender": user.gender,
                             "email": user.email,
                             "phone": user.phone,
                             "username": user.username,
                             "password": user.password,
                             "university": user.university
                             }})


@app.route('/social/api/v1.0/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """ Deletes user with user_id from the User table in database."""
    user = User.query.filter_by(id=user_id)
    if not user:
        abort(400)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'result': True})


# Posts -> Social appname
# api format appname/api/version/folder/id
@app.route("/social/api/v1.0/posts", methods=["GET"])
def posts_index():
    # Used this workaround because SQLalchemy class object can't be jsonified.
    post_list = []
    for post in posts:
        list_elem = {'id': post.id,
                     'title': post.title,
                     'body': post.body,
                     'userId': post.userId,
                     'reactions': post.reactions
                     }
        post_list.append(list_elem)
    return jsonify({'posts': post_list})


@app.route("/social/api/v1.0/posts/<int:post_id>", methods=["GET"])
def get_post(post_id):
    """
    Gets a particular post from the Post table in database.
    """
    post = Post.query.filter_by(id=post_id).first()
    if not post:
        abort(404)
    return jsonify({'post': {'id': post.id,
                             'title': post.title,
                             'body': post.body,
                             'userId': post.userId,
                             'reactions': post.reactions
                             }})


@app.route("/social/api/v1.0/posts", methods=["POST"])
def create_post():
    """ Creates new post in database. """
    if not request.json or 'title' not in request.json:
        abort(400)
    if not request.json or 'body' not in request.json:
        abort(400)
    post = Post(title=request.json['title'])
    post.body = request.json.get('body', '')
    post.userId = request.json.get('userId', None)
    #post.tags = request.json.get('tags', [])
    post.reactions = request.json.get('reactions', 0)

    db.session.add(post)
    db.session.commit()
    return jsonify({'post': {'id': post.id,
                             'title': post.title,
                             'body': post.body,
                             'userId': post.userId,
                             'reactions': post.reactions
                             }
                    }), 201


@app.route("/social/api/v1.0/posts/<int:post_id>", methods=["PUT"])
def update_post(post_id):
    """
    Updates post with post_id.
    """
    if not request.json:
        abort(400)
    post = Post.query.filter_by(id=post_id).first()
    if not post:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400)
    if 'body' in request.json and type(request.json['body']) != str:
        abort(400)
    if 'userId' in request.json and type(request.json['userId']) != int:
        abort(400)
    if 'tags' in request.json and type(request.json['tags']) != str:
        abort(400)
    if 'reactions' in request.json and type(request.json['reactions']) != int:
        abort(400)

    post.title = request.json.get('title', post.title)
    post.body = request.json.get('body', post.body)
    post.userId = request.json.get('userId', post.userId)
    # post.tags = request.json.get('tags', post.tags)
    post.reactions = request.json.get('reactions', post.reactions)
    db.session.commit()
    return jsonify({'post': {'id': post.id,
                             'title': post.title,
                             'body': post.body,
                             'userId': post.userId,
                             'reactions': post.reactions
                             }})


@app.route('/social/api/v1.0/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    """ Deletes post with post_id from the database. """
    post = Post.query.filter_by(id=post_id)
    if not post:
        abort(400)
    db.session.delete(post)
    db.session.commit()
    return jsonify({'result': True})


@app.errorhandler(404)
def not_found(error):
    """ 404 error handler."""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
