from fastapi import APIRouter

from app.services.fare_service import (
    analyze_fare
)

router = APIRouter()

@router.get("/fare/{fare}")
def fare_analysis(fare: float):

    return analyze_fare(
        fare
    )