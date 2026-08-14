from dataclasses import dataclass

@dataclass(frozen=True)
class SprintConfiguration:
    working_days: int
    working_hours_per_day: float = 6.0

    @property
    def capacity_hours(self) -> float:
        return self.working_days * self.working_hours_per_day