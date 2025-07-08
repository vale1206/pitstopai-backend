from pydantic import BaseModel
from typing import List, Literal

class TireStint(BaseModel):
    compound: Literal['soft', 'medium', 'hard']
    laps: int

class SimulationRequest(BaseModel):
    track: str
    pit_stop_time: float
    safety_car_prob: float
    tire_stints: List[TireStint]

class SimulationResponse(BaseModel):
    total_race_time: float
    details: str
