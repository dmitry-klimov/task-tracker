from app.models.task_tracker_db_obj import TaskTrackerDBObj
from app.task_tracker_app import db


class Employee(TaskTrackerDBObj):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    position = db.Column(
        db.Integer,
        db.ForeignKey('positions.id', onupdate='CASCADE', ondelete='SET NULL'),
        nullable=False
    )

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

    def __repr__(self):
        return f'{self.surname} {self.name} ({self.position})'
