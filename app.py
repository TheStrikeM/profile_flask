from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask( __name__ )
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lessoners.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "1328467456f&658*()/f845t"
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

from utils import urls, models
