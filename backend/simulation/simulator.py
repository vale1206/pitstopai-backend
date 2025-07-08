from .models import SimulationRequest, SimulationResponse

def simulate_race(data: SimulationRequest) -> SimulationResponse:
    base_lap_time = 90  # seconds
    degradation_rates = {
        "soft": 0.5,
        "medium": 0.3,
        "hard": 0.1
    }

    total_time = 0
    for stint in data.tire_stints:
        degradation = degradation_rates[stint.compound]
        for lap in range(stint.laps):
            lap_time = base_lap_time + lap * degradation
            total_time += lap_time
        total_time += data.pit_stop_time

    total_time -= data.pit_stop_time  # no pit after final stint

    return SimulationResponse(
        total_race_time=round(total_time, 2),
        details=f"Track: {data.track} | Stints: {len(data.tire_stints)}"
    )
