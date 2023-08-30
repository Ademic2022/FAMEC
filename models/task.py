from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy import Column, String, Integer, Date, Enum
from models.base_model import BaseModel, Base
import models
from enum import Enum as PythonEnum


class PriorityEnum(PythonEnum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"

class StatusEnum(PythonEnum):
    PENDING = "pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "completed"


class Task(BaseModel, Base):
    """ Task model to desscribe the tasks for users"""
    if models.storage_t == "db":
        __tablename__ = "tasks"
        __table_arg__ = {"mysql_default_charset": "latin1"}
        id = Column(Integer, primary_key=True, autoincrement=True)
        title = Column(String(255), nullable=False)
        description = Column(String(1000))
        due_date = Column(Date)
        priority = Column(Enum(PriorityEnum), default=PriorityEnum.MEDIUM)
        status = Column(Enum(StatusEnum), dafault=StatusEnum.PENDING)
        
    else:
        title = ""
        description = ""
        due_date = ""
        priority = ""
        status = ""