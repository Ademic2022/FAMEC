from .base_model import BaseModel
from sqlalchemy import Column, String, Integer, DateTime

class Task(BaseModel):
    name = Column(String(255))
    description = Column(String(255))
    due_date = Column(DateTime)
    priority = Column(Integer)
    location = Column(String(255))