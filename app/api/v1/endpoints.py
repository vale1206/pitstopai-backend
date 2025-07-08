from fastapi import APIRouter
from app.models.models import SimulationRequest, SimulationResponse
from app.services.simulator import simulate_race

router = APIRouter()

@router.post("/simulate", response_model=SimulationResponse)
async def run_simulation(data: SimulationRequest):
    result = simulate_race(data)
    return result
