from dataclasses import dataclass


@dataclass(frozen=True)
class SprintConfiguration:
    working_days: int
    working_hours_per_day: float = 6.0

    def __post_init__(self) -> None:
        if self.working_days <= 0:
            raise ValueError("Working days must be greater than zero.")

        if self.working_hours_per_day <= 0:
            raise ValueError(
                "Working hours per day must be greater than zero."
            )

    @property
    def capacity_hours(self) -> float:
        """Return the total available hours for the sprint."""
        return self.working_days * self.working_hours_per_day