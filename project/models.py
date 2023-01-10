from flask_login import UserMixin
from . import db


# UserMixin provides default implementations for the methods that Flask-Login expects user objects to have.
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
