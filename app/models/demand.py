from sqlalchemy import Column,Integer,String,Float

from app.models.base import Base

class Demand(Base):
    __tablename__ = "demand"

    id = Column(Integer, primary_key=True)

    route = Column(String)

    bookings = Column(Integer)

    month = Column(String)