from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from models.database import Base


class Weather(Base):
    __tablename__ = 'weather'
    id = Column(Integer, primary_key=True)
    A = Column(Integer)
    B = Column(Integer)
    C = Column(Float)
    D = Column(DateTime)
    E = Column(String)

    def __init__(self, A, B, C, D, E):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.E = E

    def __repr__(self):
        return '<Title %r>' % (self.title)