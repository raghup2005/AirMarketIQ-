import pandas as pd
import numpy as np
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_absolute_error, r2_score

from xgboost import XGBRegressor


# ----------------------------
# Feature Engineering
# ----------------------------

def duration_to_minutes(duration):
    hours = 0
    minutes = 0

    duration = str(duration)

    if "h" in duration:
        hours = int(duration.split("h")[0].strip())

    if "m" in duration:
        try:
            minutes = int(
                duration.split("m")[0]
                .split()[-1]
                .replace("h", "")
                .strip()
            )
        except:
            minutes = 0

    return hours * 60 + minutes


def preprocess(df):

    df = df.copy()

    # Date
    df["Date_of_Journey"] = pd.to_datetime(
        df["Date_of_Journey"],
        format="%d/%m/%Y"
    )

    df["Journey_Day"] = df["Date_of_Journey"].dt.day
    df["Journey_Month"] = df["Date_of_Journey"].dt.month

    # Departure Time
    df["Dep_Time"] = pd.to_datetime(
        df["Dep_Time"],
        format="%H:%M"
    )

    df["Dep_Hour"] = df["Dep_Time"].dt.hour
    df["Dep_Minute"] = df["Dep_Time"].dt.minute

    # Arrival Time

    arrival_hours = []
    arrival_minutes = []

    for value in df["Arrival_Time"]:

        time_part = str(value).split()[0]

        try:
            h, m = map(int, time_part.split(":"))
        except:
            h, m = 0, 0

        arrival_hours.append(h)
        arrival_minutes.append(m)

    df["Arrival_Hour"] = arrival_hours
    df["Arrival_Minute"] = arrival_minutes

    # Duration

    df["Duration_Minutes"] = (
        df["Duration"]
        .apply(duration_to_minutes)
    )

    # Stops

    stop_mapping = {
        "non-stop": 0,
        "1 stop": 1,
        "2 stops": 2,
        "3 stops": 3,
        "4 stops": 4
    }

    df["Total_Stops"] = (
        df["Total_Stops"]
        .map(stop_mapping)
        .fillna(0)
        .astype(int)
    )

    # Drop raw columns

    drop_cols = [
        "Date_of_Journey",
        "Dep_Time",
        "Arrival_Time",
        "Duration",
        "Route"
    ]

    df.drop(
        columns=drop_cols,
        inplace=True,
        errors="ignore"
    )

    return df


# ----------------------------
# Load Dataset
# ----------------------------

DATA_PATH = "data/Data_Train.xlsx"

df = pd.read_excel(DATA_PATH)

df = preprocess(df)

# ----------------------------
# Split
# ----------------------------

X = df.drop("Price", axis=1)

y = df["Price"]

categorical_cols = [
    "Airline",
    "Source",
    "Destination",
    "Additional_Info"
]

numerical_cols = [
    "Total_Stops",
    "Journey_Day",
    "Journey_Month",
    "Dep_Hour",
    "Dep_Minute",
    "Arrival_Hour",
    "Arrival_Minute",
    "Duration_Minutes"
]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(
                handle_unknown="ignore"
            ),
            categorical_cols
        ),
        (
            "num",
            "passthrough",
            numerical_cols
        )
    ]
)

model = Pipeline(
    steps=[
        (
            "preprocessor",
            preprocessor
        ),
        (
            "model",
            XGBRegressor(
                n_estimators=300,
                max_depth=8,
                learning_rate=0.05,
                subsample=0.8,
                colsample_bytree=0.8,
                random_state=42
            )
        )
    ]
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training model...")

model.fit(
    X_train,
    y_train
)

preds = model.predict(X_test)

mae = mean_absolute_error(
    y_test,
    preds
)

r2 = r2_score(
    y_test,
    preds
)

print(f"MAE: {mae:.2f}")
print(f"R2 Score: {r2:.4f}")

# ----------------------------
# Save Model
# ----------------------------

os.makedirs(
    "data/models",
    exist_ok=True
)

joblib.dump(
    model,
    "data/models/fare_model.pkl"
)

print("Model saved successfully")