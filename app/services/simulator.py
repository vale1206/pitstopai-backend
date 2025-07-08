import random
from ...simulation.models import SimulationRequest, SimulationResponse

def simulate_race(data: SimulationRequest) -> SimulationResponse:
    base_lap_times = {
        "monza": 85,
        "silverstone": 90,
        "spa": 95,
        "generic": 90
    }

    base_lap_time = base_lap_times.get(data.track.lower(), 90)
    degradation_rates = {
        "soft": 0.5,
        "medium": 0.3,
        "hard": 0.1
    }

    total_time = 0
    safety_car_active = random.random() < data.safety_car_prob
    for stint in data.tire_stints:
        degradation = degradation_rates[stint.compound]
        for lap in range(stint.laps):
            lap_time = base_lap_time + lap * degradation
            # If safety car active, lap times reduced by 20%
            if safety_car_active:
                lap_time *= 0.8
            total_time += lap_time
        total_time += data.pit_stop_time

    total_time -= data.pit_stop_time  # no pit after last stint

    details = f"Track: {data.track} | "
    details += " | ".join([f"{stint.compound} {stint.laps} laps" for stint in data.tire_stints])
    details += f" | Pit stops: {len(data.tire_stints)-1}"

    return SimulationResponse(
        total_race_time=round(total_time, 2),
        details=details
    )
