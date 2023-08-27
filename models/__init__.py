#!/usr/bin/python3
"""
initialize the models package
"""

import os
from models.engine.db_storage import DBStorage


storage_t = os.getenv("HMA_TYPE_STORAGE")
storage = DBStorage()
