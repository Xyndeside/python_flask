from models import db
from models import Student


def seed_data():
    students = [
        Student(gender="Male", year=1, age=18, group="A1"),
        Student(gender="Female", year=2, age=19, group="B2"),
        Student(gender="Male", year=3, age=20, group="C3"),
        Student(gender="Female", year=4, age=21, group="D4"),
        Student(gender="Female", year=1, age=18, group="E5"),
    ]

    db.session.add_all(students)
    db.session.commit()
