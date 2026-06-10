from fastapi import APIRouter

from app.services.market_intelligence import (
    cheapest_airline,
    expensive_airline
)

router = APIRouter()

@router.get("/cheapest")

def cheapest():

    return cheapest_airline()

@router.get("/expensive")

def expensive():

    return expensive_airline()