from decision.algorithms.greedy import GreedyPlanner
from decision.domain.sprint import SprintConfiguration
from decision.domain.task import Task

def test_planner_should_not_exceed_sprint_capacity() -> None:
    tasks = [
        Task(
            id=1,
            title="Task A",
            priority=5,
            business_value=10.0,
            estimated_hours=8.0,
        ),
        Task(
            id=2,
            title="Task B",
            priority=4,
            business_value=8.0,
            estimated_hours=8.0,
        ),
    ]

    sprint = SprintConfiguration(working_days=2)

    planner = GreedyPlanner()

    result = planner.plan(tasks, sprint)

    assert result.planned_hours <= result.capacity_hours