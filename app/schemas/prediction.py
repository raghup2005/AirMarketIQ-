from pydantic import BaseModel


class FarePredictionRequest(BaseModel):

    Airline: str
    Date_of_Journey: str

    Source: str
    Destination: str

    Route: str

    Dep_Time: str

    Arrival_Time: str

    Duration: str

    Total_Stops: str

    Additional_Info: str