from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!!!"

ENGINE = create_engine(CONNECT)
SESSION = sessionmaker(ENGINE)

Base = declarative_base()

class Test(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    city = Column(String)
    temp_lo= Column(Integer)
    date_inputed = Column(DateTime)

    def __init__(self, city, temp_lo, temp_hi, prcp, date_inputed):
        self.city = city
        self.temp_lo = temp_lo
        self.date_inputed = date_inputed
  
from sqlalchemy import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
import psycopg2

CONNECT = 'postgresql://postgres:0310@localhost:5432/test'

session = SESSION()として
all_data = session.query(Test).all()

for city in all_data:
    print(city.city)


def hello_world():
    return "<p>Hello, World!</p>"

