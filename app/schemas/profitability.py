from pydantic import BaseModel

class ProfitabilityCreate(BaseModel):
    route:str
    revenue:float
    cost:float