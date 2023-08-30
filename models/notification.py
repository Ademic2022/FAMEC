from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from sqlalchemy import (create_engine)
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from models.base_model import BaseModel, Base
from datetime import datetime
import models


class Notification(BaseModel, Base):
    if models.storage_t == "db":
        __tablename__ = "notifications"
        __table_arg__ = {"mysql_default_charset": "latin1"}
        id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
        user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
        message = Column(String(255), nullable=False)
        notification_status = Column(String(128), nullable=False, default='pending')
        user = relationship("User", backref="notifications")
        
    else:
        user_id = ""
        message = ""
        notification_status = ""
        