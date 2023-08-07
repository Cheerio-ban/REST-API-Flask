
from config import app

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

class Task(db.Model): # Model representing the task table in the database
    id = db.Column(db.Integer, primary_key=True) #Id (primary key) column
    title = db.Column(db.String, nullable=False, unique=True) # title column
    description = db.Column(db.String) # description column
    completed = db.Column(db.Boolean, default=False) # completed column

    def __repr__(self) -> str:
        return '<Task {}>'.format(self.title) # Output when being called by print or .format


class Quote(db.Model): # Model representing the quote table in the database.
    id = db.Column(db.String, primary_key=True) # id  (primary key) column
    quote = db.Column(db.String, unique=True) # quote column
    author = db.Column(db.String) # author column

    def __repr__(self) -> str:
        return "<Quote {}>".format(self.quote)


class User(db.Model):
    """
    Table for users
    """
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String, nullable=False)
    lastName = db.Column(db.String, nullable=False)
    maidenName = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    phone = db.Column(db.Integer)
    username = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String)
    university = db.Column(db.String)

    def __repr__(self) -> str:
        return "<User {}>".format(self.username)
