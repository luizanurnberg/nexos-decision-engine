from dataclasses import dataclass

from decision.domain.task import Task


@dataclass(frozen=True)
class SprintPlan:
    selected_tasks: list[Task]
    capacity_hours: float
    planned_hours: float

    @property
    def remaining_hours(self) -> float:
        return self.capacity_hours - self.planned_hours

    @property
    def utilization(self) -> float:
        if self.capacity_hours == 0:
            return 0.0

        return self.planned_hours / self.capacity_hours