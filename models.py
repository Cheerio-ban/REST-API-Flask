
from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Task {}>'.format(self.title)