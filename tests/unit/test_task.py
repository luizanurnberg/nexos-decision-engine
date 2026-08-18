import pytest

from decision.domain.task import Task, TaskStatus


def test_task_should_have_default_todo_status() -> None:
    task = Task(
        id=1,
        title="Implement authentication",
        priority=5,
        business_value=10.0,
        estimated_hours=8.0,
    )

    assert task.status == TaskStatus.TODO

def test_task_should_store_dependencies() -> None:
    task = Task(
        id=2,
        title="Create API",
        priority=4,
        business_value=8.0,
        estimated_hours=4.0,
        dependencies=[1],
    )

    assert task.dependencies == [1]

def test_task_should_reject_non_positive_id() -> None:
    with pytest.raises(ValueError):
        Task(
            id=0,
            title="Invalid task",
            priority=1,
            business_value=1.0,
            estimated_hours=2.0,
        )

def test_task_should_reject_empty_title() -> None:
    with pytest.raises(ValueError):
        Task(
            id=1,
            title="   ",
            priority=1,
            business_value=1.0,
            estimated_hours=2.0,
        )

def test_task_should_reject_negative_priority() -> None:
    with pytest.raises(ValueError):
        Task(
            id=1,
            title="Invalid priority",
            priority=-1,
            business_value=1.0,
            estimated_hours=2.0,
        )

def test_task_should_reject_negative_business_value() -> None:
    with pytest.raises(ValueError):
        Task(
            id=1,
            title="Invalid business value",
            priority=1,
            business_value=-1.0,
            estimated_hours=2.0,
        )

def test_task_should_reject_invalid_estimated_hours() -> None:
    with pytest.raises(ValueError):
        Task(
            id=1,
            title="Invalid estimation",
            priority=1,
            business_value=1.0,
            estimated_hours=0,
        )

def test_task_should_reject_self_dependency() -> None:
    with pytest.raises(ValueError):
        Task(
            id=1,
            title="Self dependency",
            priority=1,
            business_value=1.0,
            estimated_hours=2.0,
            dependencies=[1],
        )