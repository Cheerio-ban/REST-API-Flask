
from config import app

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

class Task(db.Model): # Model representing the task table in the database
    id = db.Column(db.Integer, primary_key=True) #Id (primary key) column
    title = db.Column(db.String, nullable=False, unique=True) # title column
    description = db.Column(db.String) # description column
    completed = db.Column(db.Boolean, default=False) # completed column

    def __repr__(self):
        return '<Task {}>'.format(self.title) # Output when being called by print or .format
