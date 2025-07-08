from fastapi import FastAPI
from simulation.models import SimulationRequest, SimulationResponse
from simulation.simulator import simulate_race

app = FastAPI(title="PitStopAI Backend")

@app.post("/simulate", response_model=SimulationResponse)
def simulate(data: SimulationRequest):
    return simulate_race(data)
