from decision.domain.planning import SprintPlan


def test_remaining_hours_should_be_calculated() -> None:
    plan = SprintPlan(
        selected_tasks=[],
        capacity_hours=60.0,
        planned_hours=45.0,
    )

    assert plan.remaining_hours == 15.0


def test_utilization_should_be_calculated() -> None:
    plan = SprintPlan(
        selected_tasks=[],
        capacity_hours=60.0,
        planned_hours=45.0,
    )

    assert plan.utilization == 0.75