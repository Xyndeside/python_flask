from flask import Flask
from database import db
from database.create_db import create_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


def init_db():
    create_db()


def run_app():
    init_db()
    app.run()


if __name__ == '__main__':
    run_app()
