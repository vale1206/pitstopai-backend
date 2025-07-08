from simulation.simulator import simulate_race
from simulation.models import SimulationRequest, TireStint

def test_simple_simulation():
    data = SimulationRequest(
        track="Generic",
        pit_stop_time=20.0,
        safety_car_prob=0.0,
        tire_stints=[
            TireStint(compound="soft", laps=5),
            TireStint(compound="medium", laps=5),
        ]
    )
    result = simulate_race(data)
    assert result.total_race_time > 0
    assert "Pit stop" in result.details
