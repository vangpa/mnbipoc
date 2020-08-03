# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mnbipoc.db'
app.secret_key = "titijiji!"

db = SQLAlchemy(app)
