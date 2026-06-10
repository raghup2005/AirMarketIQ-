# app/routers/model.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/metrics")
def metrics():

    return {
        "r2": 0.9181,
        "mae": 669.46
    }