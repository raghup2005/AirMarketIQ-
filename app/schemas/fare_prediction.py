from pydantic import BaseModel

class FarePredictionRequest(BaseModel):

    Airline:str

    Source:str

    Destination:str

    Total_Stops:str

    Date_of_Journey:str
    Dep_Time:str
    Arrival_Time:str
    Duration:str
    Route:str
    Additional_Info:str