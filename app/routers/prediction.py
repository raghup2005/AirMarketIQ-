from fastapi import APIRouter

from app.schemas.prediction import (
    FarePredictionRequest
)

from app.services.fare_prediction_service import (
    predict_price
)

router = APIRouter()


@router.post("/fare")
def predict_fare(
    request: FarePredictionRequest
):

    prediction = predict_price(
        request.model_dump()
    )

    return {
        "predicted_price": round(
            prediction,
            2
        )
    }