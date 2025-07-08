from fastapi import FastAPI
from app.api.v1.endpoints import router as simulation_router

app = FastAPI(title="PitStopAI Simulation API")

app.include_router(simulation_router, prefix="/api/v1")
