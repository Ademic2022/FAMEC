from .base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime


class Notification(BaseModel, Base):
    message = Column(String(255))
    due_date = Column(DateTime)
    task_id = Column(Integer, ForeignKey('tasks.id'))