from fastapi import FastAPI

from app.routers import prediction
from app.routers import market

app = FastAPI(
    title="Airline Market Intelligence"
)

app.include_router(
    prediction.router,
    prefix="/predict",
    tags=["Prediction"]
)

app.include_router(
    market.router,
    prefix="/market",
    tags=["Market"]
)

@app.get("/")
def root():
    return {
        "message": "Airline Market Intelligence API"
    }

    # app/routers/model.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/metrics")
def metrics():

    return {
        "r2": 0.9181,
        "mae": 669.46
    }