from datetime import datetime

from app.task_tracker_app import db


class TaskTrackerDBObj(db.Model):
    __abstract__ = True
    deleted_on = db.Column(db.DateTime, nullable=True)

    def delete(self):
        task = __class__().objects.filter(id=self.id)
        task.deleted_on = datetime.now()
        task.save()
        super().delete()
