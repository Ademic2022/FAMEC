from .base_model import BaseModel
from models.engine import db_storage as db


class Notification(BaseModel):
    message = db.Column(db.String(255))
    due_date = db.Column(db.DateTime)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))