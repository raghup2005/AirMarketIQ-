from app.ml.fare_anomaly import (
    FareAnomalyDetector
)

detector = FareAnomalyDetector()

sample_fares = [
    4500,
    4700,
    4900,
    5000,
    5200,
    5300,
    5400
]

detector.fit(sample_fares)

def analyze_fare(fare):

    return {
        "fare": fare,
        "is_anomaly":
        detector.detect(fare)
    }