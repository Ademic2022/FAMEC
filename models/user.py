from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from models.engine import db_storage as db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(128))