from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


if __name__ == "__main__":
    print("Space Station Data Validation")
    print("=" * 40)
    try:
        valid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True,
            notes=""
        )
        print("Valid station created:")
        print(f"ID: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size} people")
        print(f"Power: {valid_station.power_level}%")
        print(f"Oxygen: {valid_station.oxygen_level}%")
        print("Status: "
              f"{'Operational' if valid_station.is_operational else 'Down'}")
        print(f"Notes: {valid_station.notes}\n")
        print("=" * 40)

    except ValidationError as e:
        print(f"Unexpected error: {e}")

    try:
        invalid_station = SpaceStation(
            station_id="ISS002",
            name="Deep Space Nine",
            crew_size=50,
            power_level=105.0,
            oxygen_level=90.0,
            last_maintenance=datetime.now()
        )
    except ValidationError as e:
        print("Expected validation error:")
        error_msg = e.errors()[0]["msg"]
        clean_msg = error_msg.replace("Value error, ", "")
        print(clean_msg)
