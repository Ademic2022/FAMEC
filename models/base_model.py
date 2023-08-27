"""This is the base model class for FAMEC"""
from sqlalchemy.ext.declarative import declarative_base
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

time = "%Y-%m-%dT%H:%M:%S.%f"

if models.storage_t == "db":
    Base = declarative_base()
else:
    Base = object
    
class BaseModel:
    """ The basemodel class that all other classes will inherit from """
    if models.storage_t == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utc.now)
        updated_at = Column(DateTime, default=datetime.utc.now)
        