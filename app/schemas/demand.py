from pydantic import BaseModel

class DemandCreate(BaseModel):
    route:str
    bookings:int
    month:str