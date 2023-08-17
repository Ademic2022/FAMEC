from .base_model import BaseModel
from models.engine import db_storage as db

class Assignment(BaseModel):
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    due_date = db.Column(db.DateTime)