from .base_model import BaseModel
from models.engine import db_storage as db

class Task(BaseModel):
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    due_date = db.Column(db.DateTime)
    priority = db.Column(db.Integer)
    location = db.Column(db.String(255))