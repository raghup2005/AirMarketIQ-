import pandas as pd

from app.ml.model_loader import model
from app.ml.train_fare_model import preprocess


def predict_price(data):

    df = pd.DataFrame([data])

    df = preprocess(df)

    prediction = model.predict(df)

    return float(prediction[0])