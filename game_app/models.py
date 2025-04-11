from .extensions import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

class Village(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    wood = db.Column(db.Integer, default=50, nullable=False)
    stones = db.Column(db.Integer, default=50, nullable=False)
    morale = db.Column(db.Integer, default=100, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    owner = db.relationship('User', backref=db.backref('villages', lazy=True))

    def __repr__(self):
        return f"<Village {self.name}>"