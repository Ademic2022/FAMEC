""" new class for sqlAlchemy """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy import func

from models.base_model import Base

class DBStorage:
    def __init__(self):
        self.__engine = None
        self.__session = None
        self.__setup_engine()
        self.__create_session()  # Initialize the session

    def __setup_engine(self):
        user = getenv('FAMEC_MYSQL_USER')
        db_password = getenv('FAMEC_MYSQL_PWD')
        database = getenv('FAMEC_MYSQL_DB')
        host = getenv('FAMEC_MYSQL_HOST')
        env = getenv('FAMEC_ENV')

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{db_password}@{host}/{database}',
            pool_pre_ping=True
        )

        # if env == 'test':
        #     Base.metadata.drop_all(self.__engine)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)
        else:
            Base.metadata.create_all(self.__engine)


    def __create_session(self):
        if self.__session is None:
            sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
            self.__session = scoped_session(sec)
        return self.__session()

    def all(self, cls=None):
        session = self.__create_session()
        objects = {}
        
        if cls is None:
            from models.user import User # Import all model classes here
            from models.base_model import BaseModel # Import all model classes here
            from models.note import Note # Import all model classes here
            from models.notification import Notification # Import all model classes here
            from models.task import Task # Import all model classes here
            from models.user_info import UserInfo # Import all model classes here
            cls_list = [User, BaseModel, Note, Notification, Task, UserInfo]
        else:
            cls_list = [cls]
        
        for cls in cls_list:
            query = session.query(cls)
            for element in query:
                key = f"{cls.__name__}.{element.id}"
                objects[key] = element
        
        return objects

    def new(self, obj):
        session = self.__create_session()
        session.add(obj)

    def save(self):
        session = self.__create_session()
        session.commit()

    def delete(self, obj=None):
        session = self.__create_session()
        if obj:
            session.delete(obj)
    def update(self, obj):
        session = self.__create_session()
        session.merge(obj)  # Use the merge method to update the object
        session.commit()

    def count(self, obj):
        session = self.__create_session()
        count = session.query(func.count(obj.id)).scalar() # count the objects in the database
        return count

    def find_user_by_email(self, email):
        from models.user import User
        session = self.__create_session()
        query = session.query(User).filter_by(email=email).first()
        return query

    def find_user_by_id(self, id):
        from models.user import User
        session = self.__create_session()
        query = session.query(User).filter_by(id=id).first()
        return query
    
    def get_task_by_id(self, id):
        from models.task import Task
        session = self.__create_session()
        query = session.query(Task).filter_by(id=id).first()
        return query

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__create_session()

    def close(self):
        if self.__session:
            self.__session.remove()