from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    name = db.Column(db.String(64), default="Anon")
    subname = db.Column(db.String(64), default="User")
    email = db.Column(db.String(120), index=True, unique=True)
    about = db.Column(db.String(300), default="Описания нет.")
    instagram = db.Column(db.String(20), default="Не указанно", unique=True)
    github = db.Column(db.String(20), default="Не указанно", unique=True)
    vkontakte = db.Column(db.String(20), default="Не указанно", unique=True)
    facebook = db.Column(db.String(20), default="Не указанно", unique=True)
    telegram = db.Column(db.String(20), default="Не указанно", unique=True)
    site = db.Column(db.String(40), default="Не указано")
    statuse = db.Column(db.String(20), default="Не указанно")
    shool = db.Column(db.String(50), default="Не указанно")
    classs = db.Column(db.String(50), default="Не указанно")
    password_hash = db.Column(db.String(128)) #Learner

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return Users.query.get(int(id))