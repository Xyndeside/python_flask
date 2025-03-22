from flask import Flask, render_template
from database.models import db, Book

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/books')
def show_books():
    books = Book.query.all()
    return render_template('books.html', books=books)


def run_app():
    app.run()


if __name__ == '__main__':
    run_app()
