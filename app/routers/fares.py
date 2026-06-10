from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.fare import Fare
from app.schemas.fare import FareCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_fare(
    fare: FareCreate,
    db: Session = Depends(get_db)
):
    obj = Fare(**fare.dict())

    db.add(obj)

    db.commit()

    db.refresh(obj)

    return obj

@router.get("/")
def get_fares(
    db: Session = Depends(get_db)
):
    return db.query(Fare).all()