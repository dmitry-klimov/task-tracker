from flask import request
from flask_apispec import doc, MethodResource, marshal_with
from flask_restful import Resource
from marshmallow import Schema, fields

from app.models import Task
from app.models.task import TaskStatuses, TaskStatusesChoices
from app.task_tracker_app import db


class TasksAPIGetResponseSchema(Schema):
    priority = fields.Str(description='Приоритет задачи')
    description = fields.Str(description='Постановка задачи')
    parent_task = fields.Str(description='Основная задача')
    employee = fields.Str(default=TaskStatuses.UNASSIGNED[0], description='Исполнитель')
    due_to = fields.DateTime(description='Срок исполнения')
    status = fields.Str(description='Текущий статус задачи')


class TasksAPIPostRequestSchema(Schema):
    priority = fields.Str(description='Приоритет', required=True)
    description = fields.Str(description='Задача', required=True)
    parent_task = fields.Str(description='Основная задача', required=False, default=None)
    employee = fields.Str(default=TaskStatuses.UNASSIGNED[0], description='Исполнитель', required=False)
    due_to = fields.DateTime(description='Срок исполнения', required=True)


class TasksAPIPutRequestSchema(Schema):
    priority = fields.Str(description='Приоритет', required=False)
    description = fields.Str(description='Задача', required=False)
    parent_task = fields.Str(description='Основная задача', required=False)
    employee = fields.Str(default=TaskStatuses.UNASSIGNED[0], description='Исполнитель', required=False)
    due_to = fields.DateTime(description='Срок исполнения', required=False)
    status = fields.Str(description='Текущий статус задачи', required=False)


class TasksAPIDeleteRequestSchema(Schema):
    id = fields.Int(required=True)


API_NAME = 'Tasks API'
API_TAGS = ['Tasks']


class TasksAPI(MethodResource, Resource):
    @marshal_with(TasksAPIGetResponseSchema)
    @doc(description=API_NAME, tags=API_TAGS)
    def get(self):
        tasks = Task.query.filter(Task.deleted_on==None)
        results = [
            {
                "priority": task.priority,
                'parent_task': task.parent_task,
                "description": task.description,
                'employee': task.employee,
                'due_to': task.due_to,
                'status': task.status
            } for task in tasks
        ]

        return {"count": len(results), "tasks": results}

    @marshal_with(TasksAPIPostRequestSchema)
    @doc(description=API_NAME, tags=API_TAGS)
    def post(self):
        if request.is_json:
            data = request.get_json()
            new_task = Task(
                priority=data['priority'],
                parent_task=data['parent_task'],  # TODO add searching parent task id?
                description=data['description'],
                employee=data['employee'],
                due_to=data['due_to'],
            )
            db.session.add(new_task)
            db.session.commit()
            return {"message": f"Task {new_task.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    @marshal_with(TasksAPIPutRequestSchema)
    @doc(description=API_NAME, tags=API_TAGS)
    def put(self):
        if request.is_json:
            data = request.get_json()
            task = Task.oblects.find(id=data['id'])
            if task:  # TODO accomplish updating task
                task = Task(
                    priority=data['priority'],
                    parent_task=data['parent_task'],  # TODO add searching parent task id?
                    description=data['description'],
                    employee=data['employee'],
                    due_to=data['due_to'],
                )
                return {"message": f"Task {task.name} has been updated successfully."}
            else:
                return {"message": f"Task {task.name} not found."}
        else:
            return {"error": "The request payload is not in JSON format"}

    @marshal_with(TasksAPIDeleteRequestSchema)
    @doc(description=API_NAME, tags=API_TAGS)
    def delete(self):
        if request.is_json:
            data = request.get_json()
            task = Task.oblects.find(id=data['id'])
            if task:
                task.delete()
                task.save()
                return {"message": f"Task {task.name} has been deleted successfully."}
            else:
                return {"message": f"Task {task.name} not found."}
        else:
            return {"error": "The request payload is not in JSON format"}

