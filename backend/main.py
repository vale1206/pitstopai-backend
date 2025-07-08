from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Literal

app = FastAPI(title="PitStopAI Backend")

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

@app.post("/simulate", response_model=SimulationResponse)
def simulate_race(data: SimulationRequest):
    base_lap_time = 90  # seconds (example)
    degradation_rates = {
        "soft": 0.5,
        "medium": 0.3,
        "hard": 0.1
    }
    total_time = 0
    for stint in data.tire_stints:
        degradation = degradation_rates[stint.compound]
        for lap in range(stint.laps):
            total_time += base_lap_time + (lap * degradation)
        total_time += data.pit_stop_time  # pit stop penalty
    total_time -= data.pit_stop_time  # no pit stop after final stint
    details = f"Simulated race on {data.track} with {len(data.tire_stints)} stints."
    return SimulationResponse(total_race_time=round(total_time, 2), details=details)
