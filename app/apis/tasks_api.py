from flask import request
from flask_apispec import doc, MethodResource
from flask_restful import Resource

from app.models import Task
from app.task_tracker_app import db


# awesome_response_schema = dict(
#     message=fields.String(default='')
# )


class TasksAPI(MethodResource, Resource):
    # @marshal_with(awesome_response_schema)
    @doc(description='Tasks API', tags=['Tasks'])
    def get(self):
        tasks = Task.query.all()
        results = [
            {
                "priority": task.priority,
                "description": task.description,
                'employee': task.employee,
                'due_to': task.due_to,
                'status': task.status
            } for task in tasks
        ]

        return {"count": len(results), "tasks": results}

    @doc(description='Tasks API', tags=['Tasks'])
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
