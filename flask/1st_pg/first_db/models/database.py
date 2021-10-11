from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE = 'postgresql'
USER ='postgres'
PASSWORD = '0310'
HOST = 'localhost'
PORT = '5432'
DB_NAME = 'test'

CONNECT_STR = '{}://{}:{}@{}:{}/{}'.format(DATABASE, USER, PASSWORD, HOST, PORT, DB_NAME)

ENGINE = create_engine(CONNECT_STR)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=ENGINE))
Base = declarative_base()
Base.query = db_session.query_property()
