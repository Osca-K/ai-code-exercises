from datetime import datetime

from models import TaskStatus, TaskPriority

def calculate_task_score(task):

    """
    Calculate a composite priority score for a task based on multiple weighted factors.

    The score reflects urgency, importance, completion status, context tags, and recent activity.
    This is used to sort and prioritize tasks in a task management system.

    Parameters
    ----------
    task : Task
        The task object to score. Expected to have:
            - priority (TaskPriority): Priority level (LOW, MEDIUM, HIGH, URGENT)
            - due_date (datetime or None): Due date, or None
            - status (TaskStatus): Current status (e.g., DONE, REVIEW)
            - tags (list of str): Associated tags
            - updated_at (datetime): Last updated timestamp

    Returns
    -------
    int
        The calculated priority score. Higher means higher priority.

    Raises
    ------
    AttributeError
        If the task object lacks required attributes.

    Example
    -------
    >>> task = Task(priority=TaskPriority.HIGH, due_date=datetime(2026, 2, 15), status=TaskStatus.ACTIVE, tags=['urgent'], updated_at=datetime.now())
    >>> score = calculate_task_score(task)
    >>> print(score)
    63

    Notes
    -----
    - Overdue tasks: +35 points
    - Due today: +20, soon: +15, within a week: +10
    - DONE: -50, REVIEW: -15
    - Tags 'blocker', 'critical', 'urgent': +8
    - Updated <24h ago: +5
    """
    # Base priority weights (exponential scaling for greater separation)
    priority_weights = {
        TaskPriority.LOW: 1,
        TaskPriority.MEDIUM: 2,
        TaskPriority.HIGH: 4,
        TaskPriority.URGENT: 6
    }

    # 1. Base score from priority
    score = priority_weights.get(task.priority, 0) * 10

    # 2. Add due date factor (higher score for tasks due sooner)
    if task.due_date:
        days_until_due = (task.due_date - datetime.now()).days
        if days_until_due < 0:  # Overdue tasks
            score += 35
        elif days_until_due == 0:  # Due today
            score += 20
        elif days_until_due <= 2:  # Due in next 2 days
            score += 15
        elif days_until_due <= 7:  # Due in next week
            score += 10

    # 3. Reduce score for completed or review tasks
    if task.status == TaskStatus.DONE:
        score -= 50  # Completed tasks are deprioritized
    elif task.status == TaskStatus.REVIEW:
        score -= 15  # In-review tasks are less urgent

    # 4. Boost score for critical tags
    if any(tag in ["blocker", "critical", "urgent"] for tag in task.tags):
        score += 8  # Critical context tags

    # 5. Boost score for recently updated tasks
    days_since_update = (datetime.now() - task.updated_at).days
    if days_since_update < 1:
        score += 5  # Recently modified tasks

    return score

def sort_tasks_by_importance(tasks):
    """Sort tasks by calculated importance score (highest first)."""
    task_scores = [(calculate_task_score(task), task) for task in tasks]
    # Use key parameter to tell sorted() to only compare the scores (first element of tuple)
    sorted_tasks = [task for _, task in sorted(task_scores, key=lambda x: x[0], reverse=True)]
    return sorted_tasks

def get_top_priority_tasks(tasks, limit=5):
    """Return the top N priority tasks."""
    sorted_tasks = sort_tasks_by_importance(tasks)
    return sorted_tasks[:limit]
