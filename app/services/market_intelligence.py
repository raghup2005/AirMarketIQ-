import pandas as pd

df = pd.read_excel(
    "data/Data_Train.xlsx"
)

def cheapest_airline():

    result = (
        df.groupby("Airline")
        ["Price"]
        .mean()
        .sort_values()
        .head(1)
    )

    return {
        "airline": result.index[0],
        "average_price":
        float(result.iloc[0])
    }

def expensive_airline():

    result = (
        df.groupby("Airline")
        ["Price"]
        .mean()
        .sort_values(
            ascending=False
        )
        .head(1)
    )

    return {
        "airline": result.index[0],
        "average_price":
        float(result.iloc[0])
    }