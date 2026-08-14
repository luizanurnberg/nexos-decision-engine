from decision.domain.planning import SprintPlan
from decision.domain.sprint import SprintConfiguration
from decision.domain.task import Task, TaskStatus

class GreedyPlanner:

    def __init__(
        self,
        priority_weight: float = 0.7,
        business_value_weight: float = 0.3,
    ) -> None:
        if priority_weight < 0:
            raise ValueError("priority_weight must be non-negative.")

        if business_value_weight < 0:
            raise ValueError("business_value_weight must be non-negative.")

        if priority_weight + business_value_weight == 0:
            raise ValueError(
                "At least one scoring weight must be greater than zero."
            )

        self._priority_weight = priority_weight
        self._business_value_weight = business_value_weight

    def plan(
        self,
        tasks: list[Task],
        sprint: SprintConfiguration,
    ) -> SprintPlan:

        selected_tasks: list[Task] = []
        selected_task_ids: set[int] = set()

        remaining_hours = sprint.capacity_hours
        task_map = {task.id: task for task in tasks}

        while True:
            eligible_tasks = self._get_eligible_tasks(
                tasks=tasks,
                task_map=task_map,
                selected_task_ids=selected_task_ids,
            )

            if not eligible_tasks:
                break

            eligible_tasks.sort(
                key=self._calculate_score,
                reverse=True,
            )

            selected_task = self._find_task_that_fits(
                tasks=eligible_tasks,
                remaining_hours=remaining_hours,
            )

            if selected_task is None:
                break

            selected_tasks.append(selected_task)
            selected_task_ids.add(selected_task.id)

            remaining_hours -= selected_task.estimated_hours

        planned_hours = sprint.capacity_hours - remaining_hours

        return SprintPlan(
            selected_tasks=selected_tasks,
            capacity_hours=sprint.capacity_hours,
            planned_hours=planned_hours,
        )

    def _calculate_score(self, task: Task) -> float:

        if task.estimated_hours <= 0:
            return 0.0

        weighted_value = (
            task.priority * self._priority_weight
            + task.business_value * self._business_value_weight
        )

        return weighted_value / task.estimated_hours

    def _get_eligible_tasks(
        self,
        tasks: list[Task],
        task_map: dict[int, Task],
        selected_task_ids: set[int],
    ) -> list[Task]:

        return [
            task
            for task in tasks
            if self._is_eligible(
                task=task,
                task_map=task_map,
                selected_task_ids=selected_task_ids,
            )
        ]

    def _is_eligible(
        self,
        task: Task,
        task_map: dict[int, Task],
        selected_task_ids: set[int],
    ) -> bool:

        if task.status in {
            TaskStatus.DONE,
            TaskStatus.BLOCKED,
        }:
            return False

        return self._dependencies_are_satisfied(
            task=task,
            task_map=task_map,
            selected_task_ids=selected_task_ids,
        )

    def _dependencies_are_satisfied(
        self,
        task: Task,
        task_map: dict[int, Task],
        selected_task_ids: set[int],
    ) -> bool:

        for dependency_id in task.dependencies:
            dependency = task_map.get(dependency_id)

            if dependency is None:
                return False

            if dependency.status == TaskStatus.DONE:
                continue

            if dependency.id in selected_task_ids:
                continue

            return False

        return True

    @staticmethod
    def _find_task_that_fits(
        tasks: list[Task],
        remaining_hours: float,
    ) -> Task | None:

        for task in tasks:
            if task.estimated_hours <= remaining_hours:
                return task

        return None