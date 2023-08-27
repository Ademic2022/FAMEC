from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
import models


class Task(BaseModel, Base):
    """ Task model to desscribe the tasks for users"""