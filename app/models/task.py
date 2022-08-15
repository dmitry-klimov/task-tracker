import enum

from app.models.choice_type import ChoiceType
from app.models.task_tracker_db_obj import TaskTrackerDBObj
from app.task_tracker_app import db


class TaskStatuses:
    UNASSIGNED = "unassigned",
    ASSIGNED = 'assigned',
    IN_PROGRESS = 'in_progress',
    ON_HOLD = 'on_hold',
    DONE = 'accomplished'


class TaskStatusesChoices(enum.Enum):
    TaskStatuses.UNASSIGNED = "Не назначено",
    TaskStatuses.ASSIGNED = "Назначено",
    TaskStatuses.IN_PROGRESS = "В работе",
    TaskStatuses.ON_HOLD = "Ожидание",
    TaskStatuses.DONE = "Выполнено",


class Task(TaskTrackerDBObj):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    parent_task = db.Column(
        db.Integer,
        db.ForeignKey('tasks.id', onupdate='CASCADE', ondelete='CASCADE'),
        nullable=True
    )
    employee = db.Column(
        db.Integer,
        db.ForeignKey('employees.id', onupdate='CASCADE', ondelete='CASCADE'),
        nullable=True
    )
    status = db.Column(
        ChoiceType(TaskStatusesChoices),
        nullable=False
    )
    due_to = db.Column(db.DateTime, nullable=False)

    def __init__(self, description, parent_task, employee, due_to, priority):
        self.description = description
        self.employee = employee
        self.parent_task = parent_task
        self.due_to = due_to
        self.priority = priority
        self.status = TaskStatuses.UNASSIGNED

    def __repr__(self):
        return f'{self.surname} {self.name}'
