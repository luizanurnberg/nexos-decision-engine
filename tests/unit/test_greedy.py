from decision.domain.task import TaskStatus
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

def test_planner_should_prioritize_higher_scoring_tasks() -> None:
    high_priority_task = Task(
        id=1,
        title="High Priority",
        priority=5,
        business_value=10.0,
        estimated_hours=4.0,
    )

    low_priority_task = Task(
        id=2,
        title="Low Priority",
        priority=1,
        business_value=2.0,
        estimated_hours=4.0,
    )

    sprint = SprintConfiguration(working_days=1)

    planner = GreedyPlanner()

    result = planner.plan(
        [low_priority_task, high_priority_task],
        sprint,
    )

    assert result.selected_tasks[0].id == high_priority_task.id
    
def test_planner_should_respect_dependencies() -> None:
    database_task = Task(
        id=1,
        title="Create database",
        priority=5,
        business_value=10.0,
        estimated_hours=4.0,
    )

    api_task = Task(
        id=2,
        title="Create API",
        priority=5,
        business_value=10.0,
        estimated_hours=2.0,
        dependencies=[1],
    )

    sprint = SprintConfiguration(working_days=1)

    planner = GreedyPlanner()

    result = planner.plan(
        [api_task, database_task],
        sprint,
    )

    selected_ids = [
        task.id
        for task in result.selected_tasks
    ]

    assert selected_ids == [1, 2]


def test_planner_should_not_select_blocked_tasks() -> None:
    blocked_task = Task(
        id=1,
        title="Blocked task",
        priority=5,
        business_value=10.0,
        estimated_hours=2.0,
        status=TaskStatus.BLOCKED,
    )

    sprint = SprintConfiguration(working_days=1)

    planner = GreedyPlanner()

    result = planner.plan(
        [blocked_task],
        sprint,
    )

    assert result.selected_tasks == []

def test_planner_should_not_select_completed_tasks() -> None:
    completed_task = Task(
        id=1,
        title="Completed task",
        priority=5,
        business_value=10.0,
        estimated_hours=2.0,
        status=TaskStatus.DONE,
    )

    sprint = SprintConfiguration(working_days=1)

    planner = GreedyPlanner()

    result = planner.plan(
        [completed_task],
        sprint,
    )

    assert result.selected_tasks == []