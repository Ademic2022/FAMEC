""" new class for sqlAlchemy """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from models.base_model import Base


class DBStorage():
    """ create tables in environmental"""
    __engine = None
    __session = None
    
    def __init__(self):
        user = getenv('FAMEC_MYSQL_USER')
        db_password = getenv('FAMEC_MYSQL_PWD')
        database = getenv('FAMEC_MYSQL_DB')
        host = getenv('FAMEC_MYSQL_HOST')
        env = getenv('FAMEC_ENV')

        self.__engine  = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, db_password, host, database),
                                      pool_pre_ping=True)
        
        if env == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for element in query:
                key = "{}.{}".format(type(element).__name__, element.id)
                dic[key] = element
        else:
            lista = ['model classes here']
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)
    
    def new(self, obj):
        """add a new element in the table
        """
        self.__session.add(obj)
    def save (self):
        """save changes
        """
        self.__session.commit()
    def delete(self, obj = None):
        """delete an element in the table
        """
        if obj:
            self.__session.delete(obj)

    def find_user_by_email(self, email):
        from models.user import User
        """Find a user by their email"""
        query = self.__session.query(User).filter_by(email=email).first()
        return query

    def reload(self):
        """configuration
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """ calls remove()
        """
        self.__session.close()