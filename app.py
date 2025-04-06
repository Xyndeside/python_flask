from flask import Flask, render_template
from flask_migrate import Migrate

from database.models import db, Student

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/students')
def get_students():
    students = Student.query.all()
    return render_template('students.html', students=students)


def run_app():
    app.run()


if __name__ == '__main__':
    run_app()
