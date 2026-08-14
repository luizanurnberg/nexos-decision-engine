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