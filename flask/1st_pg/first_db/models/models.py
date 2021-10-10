from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from models.database import Base
from datetime import datetime


class Weather(Base):
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

    def __repr__(self):
        return '<Title %r>' % (self.title)