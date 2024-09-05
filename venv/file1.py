from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/flask_1'
db = SQLAlchemy(app)
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable = False)

    def __init__(self, username, email):
        self.id = id
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
@app.route("/")
def hello_world():
    return "<p>Hello, World!, Bye--Bye!!!</p>"
def create_app():
    app = Flask(__name__)
    db.init_app(app)
    return app

def my_function():
    with app.app_context():
        user = db.User('postgres')
        db.session.add('postgres')
        db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)
