import pytest

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

def test_sprint_should_reject_zero_working_days() -> None:
    with pytest.raises(ValueError):
        SprintConfiguration(working_days=0)

def test_sprint_should_reject_negative_working_days() -> None:
    with pytest.raises(ValueError):
        SprintConfiguration(working_days=-1)

def test_sprint_should_reject_invalid_working_hours() -> None:
    with pytest.raises(ValueError):
        SprintConfiguration(
            working_days=10,
            working_hours_per_day=0,
        )