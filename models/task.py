from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Enum, ForeignKey, Integer
from models.base_model import BaseModel, Base
import models
from enum import Enum as PythonEnum

class Task(BaseModel, Base):
    """ Task model to describe the tasks for users"""
    if models.storage_t == "db":
        __tablename__ = "tasks"
        __table_args__ = {"mysql_default_charset": "latin1"}
        title = Column(String(255), nullable=False)
        description = Column(String(1000))
        due_date = Column(String(50))
        priority = Column(Integer, default=1)
        status = Column(Integer, default=0)
        
        # Define the foreign key relationship to the User model
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        user = relationship('User', back_populates='tasks')
    else:
        title = ""
        description = ""
        due_date = ""
        priority = ""
        status = ""
