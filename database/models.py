from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(20), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    group = db.Column(db.String(50), nullable=False)
