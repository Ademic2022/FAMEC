#!/usr/bin/venv python3
from base_model import Base, BaseModel
from sqlalchemy import Column, String, Integer
# import models
# import sqlalchemy



class User(BaseModel, Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255), unique=True)
    password = Column(String(128))