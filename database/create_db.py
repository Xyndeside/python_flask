from flask import Flask

from seed import seed_data
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_data()
        db.session.commit()