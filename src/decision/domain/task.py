from dataclasses import dataclass, field
from enum import Enum


class TaskStatus(Enum):

    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
    BLOCKED = "BLOCKED"


@dataclass(frozen=True)
class Task:

    id: int
    title: str
    priority: int
    business_value: float
    estimated_hours: float
    status: TaskStatus = TaskStatus.TODO
    dependencies: list[int] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.id <= 0:
            raise ValueError("Task id must be greater than zero.")

        if not self.title.strip():
            raise ValueError("Task title cannot be empty.")

        if self.priority < 0:
            raise ValueError("Task priority cannot be negative.")

        if self.business_value < 0:
            raise ValueError("Task business value cannot be negative.")

        if self.estimated_hours <= 0:
            raise ValueError("Task estimated hours must be greater than zero.")

        if self.id in self.dependencies:
            raise ValueError("A task cannot depend on itself.")