from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
import models
import hashlib


class User(BaseModel, Base):
    """ Represent the user details for the user class"""
    if models.storage_t == "db":
        __tablename__ = 'users'
        __table_arg__ = {"mysql_default_charset": "latin1"}
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        username = Column(String(128), nullable=False)
        family_members = Column(String(255), nullable=False)
    else:
        email = ""
        password = ""
        username = ""
        family_members = ""
        
    def __init__(self, *args, **kwargs):
        """Initializes the user if a passwordis created
        or the user is updated"""
        if "password" in kwargs:
            kwargs["password"] = hashlib.md5(
                kwargs["password"].encode()).hexdigest()
            super().__init__(*args, **kwargs)
                           
    def save_pwd(self):
        """saving the password to the database after hashing it"""
        if "password" in self.__dict__:
            self.password = hashlib.md5(self.password.encode()).hexdigest()
            super().save()
            
    def add_fam_member(self, member_name):
        """ Adding family members to the list"""
        self.family_members = []
        self.family_members.append(member_name)
        
    def get_fam_mem(self):
        """ get the list of family members"""
        return self.family_members
    