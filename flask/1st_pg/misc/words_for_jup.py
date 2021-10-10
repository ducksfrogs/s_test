import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Test(Base):
    __tablename__ = 'weather2'
    id = Column(Integer, primary_key=True)
    city = Column(String)
    temp_lo = Column(Integer)
    temp_hi = Column(Integer)
    prcp = Column(Float)
    date_inputed = Column(DateTime)

    def __init__(self, city, temp_lo, temp_hi, prcp, date_inputed):
        self.city = city
        self.temp_lo = temp_lo
        self.temp_hi = temp_hi
        self.prcp = prcp
        self.date_inputed = date_inputed
    
    def __str__(self):
        return 'id:{}, city:{}, temp_lo:{}, temp_hi:{}, prcp:{}, date_inputed:{}'.format(self.id, self.city, self.temp_lo, self.temp_hi, self.prcp, self.date_inputed)

        



DATABASE = 'postgresql'
USER ='postgres'
PASSWORD = ''
HOST = 'localhost'
PORT = '5432'
DB_NAME = 'test'

CONNECT_STR = '{}://{}:{}@{}:{}/{}'.format(DATABASE, USER, PASSWORD, HOST, PORT, DB_NAME)

ENGINE = create_engine(CONNECT_STR)
SESSION = sessionmaker(ENGINE)

inc = Test(city='Utsunomiya',temp_lo=30, temp_hi=45, prcp=0.24, date_inputed='2021-10-8')