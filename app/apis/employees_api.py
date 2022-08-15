from flask import request
from flask_apispec import doc, MethodResource
from flask_restful import Resource

from app.models import Task, Employee
from app.task_tracker_app import db


# awesome_response_schema = dict(
#     message=fields.String(default='')
# )

API_NAME = 'Employees API'
API_TAGS = ['Employees']


class EmployeesAPI(MethodResource, Resource):
    # @marshal_with(awesome_response_schema)
    @doc(description=API_NAME, tags=API_TAGS)
    def get(self):
        employees = Employee.query.all()
        results = [
            {
                "name": employee.name,
                "surname": employee.surname,
                'position': employee.position.name,
                'tasks': Task.query.filter().count(),
            } for employee in employees
        ]

        return {"count": len(results), "tasks": results}

    @doc(description=API_NAME, tags=API_TAGS)
    def post(self):
        if request.is_json:
            data = request.get_json()
            new_employee = Employee(
                name=data['name'],
                surname=data['surname'],
                position=data['position'],
            )
            db.session.add(new_employee)
            db.session.commit()
            return {"message": f"Employee {new_employee.name} {new_employee.surname} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}
