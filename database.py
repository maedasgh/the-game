from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app=Flask(__name__)
db_path = os.path.join(os.path.dirname(__file__), 'db.db')
db_uri = 'sqlite:///{}'.format(db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False,primary_key=True)
    password = db.Column(db.String(30), unique=False, nullable=False)
    score = db.Column(db.String(30), unique=False, nullable=False)

