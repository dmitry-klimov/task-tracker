from app.apis import TasksAPI, PositionsAPI, EmployeesAPI
from app.task_tracker_app import app, api, docs

__all__ = [
    'TasksAPI',
    'EmployeesAPI',
    'PositionsAPI',
    'app'
]

api.add_resource(EmployeesAPI, '/employees')
api.add_resource(TasksAPI, '/tasks')
api.add_resource(PositionsAPI, '/positions')

docs.register(PositionsAPI)
docs.register(EmployeesAPI)
docs.register(TasksAPI)
