from decision.domain.sprint import SprintConfiguration

def test_sprint_capacity_should_be_calculated_from_working_days() -> None:
    sprint = SprintConfiguration(working_days=10)

    assert sprint.capacity_hours == 60.0


def test_sprint_should_support_custom_working_hours() -> None:
    sprint = SprintConfiguration(
        working_days=10,
        working_hours_per_day=7.0,
    )

    assert sprint.capacity_hours == 70.0