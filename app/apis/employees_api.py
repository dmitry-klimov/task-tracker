from flask import request
from flask_apispec import doc, MethodResource
from flask_restful import Resource

from app.apis.common import NOT_JSON_ERR_MSG
from app.models import Task, Employee
from app.task_tracker_app import db


API_NAME = 'Employees API'
API_TAGS = ['Employees']


class EmployeesAPI(MethodResource, Resource):
    @doc(description=API_NAME, tags=API_TAGS)
    def get(self):
        employees = Employee.query.filter(Employee.deleted_on == None)
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
        if not request.is_json:
            return NOT_JSON_ERR_MSG

        data = request.get_json()
        new_employee = Employee(
            name=data['name'],
            surname=data['surname'],
            position=data['position'],
        )
        db.session.add(new_employee)
        db.session.commit()
        return {"message": f"Employee {new_employee.name} {new_employee.surname} has been created successfully."}
