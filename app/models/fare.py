from sqlalchemy import Column,Integer,String,Float,DateTime
from datetime import datetime

from app.models.base import Base

class Fare(Base):
    __tablename__ = "fares"

    id = Column(Integer, primary_key=True, index=True)

    airline = Column(String)
    source = Column(String)
    destination = Column(String)

    fare = Column(Float)

    collected_at = Column(
        DateTime,
        default=datetime.utcnow
    )