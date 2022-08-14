from flask import request

from app import app, db
from app.models import Task


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/tasks', methods=['POST', 'GET'])
def handle_tasks():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_task = Task(name=data['name'], model=data['model'], doors=data['doors'])
            db.session.add(new_task)
            db.session.commit()
            return {"message": f"car {new_car.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        tasks = Task.query.all()
        results = [
            {
                "name": car.name,
                "model": car.model,
                "doors": car.doors
            } for task in tasks]

        return {"count": len(results), "cars": results}
