from sqlalchemy import Column,Integer,String,Float

from app.models.base import Base

class Profitability(Base):
    __tablename__ = "profitability"

    id = Column(Integer, primary_key=True)

    route = Column(String)

    revenue = Column(Float)

    cost = Column(Float)

    profit = Column(Float)