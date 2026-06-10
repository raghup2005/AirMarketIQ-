# RouteIQ 

### Airline Market Intelligence Platform

RouteIQ is a full-stack airline analytics platform that leverages Machine Learning and Business Intelligence to provide fare prediction, competitor benchmarking, route analytics, and pricing intelligence for airlines.

Built using FastAPI, XGBoost, Streamlit, and PostgreSQL, RouteIQ helps analyze airline pricing trends and generate actionable business insights from real-world flight data.

---

## Features

### Fare Prediction

* Predict airline ticket prices in real-time
* Powered by XGBoost Regression
* R² Score: **0.918**
* Mean Absolute Error (MAE): **₹669**

### Competitor Intelligence

* Compare average fares across airlines
* Identify cheapest and premium carriers
* Analyze pricing strategies

### Route Analytics

* Route-level fare analysis
* Top-performing routes
* Most expensive and cheapest routes

### Executive Dashboard

* Interactive business intelligence dashboards
* KPI tracking
* Fare trend visualization
* Airline benchmarking

---

## Dataset

Flight Fare Prediction Dataset

* Records: **10,683**
* Features:

  * Airline
  * Source
  * Destination
  * Route
  * Date of Journey
  * Departure Time
  * Arrival Time
  * Duration
  * Total Stops
  * Additional Information
  * Price (Target)

---

## Tech Stack

### Backend

* FastAPI
* Uvicorn

### Machine Learning

* XGBoost
* Scikit-Learn
* Pandas
* NumPy

### Dashboard

* Streamlit
* Plotly

### Database

* PostgreSQL
* SQLAlchemy

### Deployment

* Docker

---

## Project Structure

```text
routeiq/

├── app/
│   ├── ml/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   ├── models/
│   └── main.py
│
├── dashboard/
│
├── data/
│   ├── Data_Train.xlsx
│   └── models/
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## Model Performance

| Metric       | Value          |
| ------------ | -------------- |
| R² Score     | 0.918          |
| MAE          | ₹669           |
| Dataset Size | 10,683 Flights |

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/routeiq.git
cd routeiq
```

### Create Virtual Environment

```bash
python -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Train Model

```bash
python app/ml/train_fare_model.py
```

Model artifact:

```text
data/models/fare_model.pkl
```

---

## Run FastAPI

```bash
uvicorn app.main:app --reload
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Sample Prediction Request

```json
{
  "Airline": "IndiGo",
  "Date_of_Journey": "24/03/2019",
  "Source": "Banglore",
  "Destination": "New Delhi",
  "Route": "BLR → DEL",
  "Dep_Time": "22:20",
  "Arrival_Time": "01:10",
  "Duration": "2h 50m",
  "Total_Stops": "non-stop",
  "Additional_Info": "No info"
}
```

---

## Future Enhancements

* Real-time fare monitoring
* Demand forecasting
* Route profitability scoring
* Airline recommendation engine
* Competitor alert system
* Cloud deployment (AWS)

---

## Resume Impact

RouteIQ demonstrates:

* Machine Learning
* Feature Engineering
* API Development
* Business Analytics
* Data Visualization
* Software Engineering
* Airline Pricing Intelligence

making it highly relevant for Data Science, Machine Learning, Business Analytics, and Revenue Management roles.

---

## Author

Ritwik

Built to explore the intersection of Machine Learning, Business Intelligence, and Airline Analytics.
