from .base_model import BaseModel
from sqlalchemy import Column, DateTime, ForeignKey, Integer

class Assignment(BaseModel):
    task_id = Column(Integer, ForeignKey('tasks.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    due_date = Column(DateTime)