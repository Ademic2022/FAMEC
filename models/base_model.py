from datetime import datetime
import models
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base


if models.storage_t == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)