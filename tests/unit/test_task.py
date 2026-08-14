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