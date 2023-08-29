from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from os import getenv

if getenv("FAMEC_MYSQL_DB") == "db":
    storage = DBStorage()