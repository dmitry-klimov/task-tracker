from flask import request
from flask_apispec import doc, MethodResource
from flask_restful import Resource

from app.models import Position
from app.task_tracker_app import db


# awesome_response_schema = dict(
#     message=fields.String(default='')
# )


class PositionsAPI(MethodResource, Resource):
    # @marshal_with(awesome_response_schema)
    @doc(description='Positions API', tags=['Positions'])
    def get(self):
        positions = Position.query.all()
        results = [
            {
                "position": position.name,
            } for position in positions
        ]

        return {"count": len(results), "positions": results}

    @doc(description='Positions API', tags=['Positions'])
    def post(self):
        if request.is_json:
            data = request.get_json()
            new_pos = Position(
                name=data['name'],
            )
            db.session.add(new_pos)
            db.session.commit()
            return {"message": f"Position {new_pos.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}
