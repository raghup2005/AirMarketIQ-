from pydantic import BaseModel

class FareCreate(BaseModel):
    airline:str
    source:str
    destination:str
    fare:float

class FareResponse(FareCreate):
    id:int

    class Config:
        from_attributes = True