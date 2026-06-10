import pandas as pd

from sklearn.ensemble import IsolationForest

class FareAnomalyDetector:

    def __init__(self):

        self.model = IsolationForest(
            contamination=0.05,
            random_state=42
        )

    def fit(self, fares):

        df = pd.DataFrame({
            "fare": fares
        })

        self.model.fit(df)

    def detect(self, fare):

        result = self.model.predict(
            [[fare]]
        )

        return result[0] == -1