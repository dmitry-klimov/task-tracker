from flask import request
from flask_apispec import doc, MethodResource
from flask_restful import Resource

from app.apis.common import NOT_JSON_ERR_MSG
from app.models import Position
from app.task_tracker_app import db


API_NAME = 'Positions API'
API_TAGS = ['Positions']


class PositionsAPI(MethodResource, Resource):
    # @marshal_with(awesome_response_schema)
    @doc(description=API_NAME, tags=API_TAGS)
    def get(self):
        positions = Position.query.all()
        results = [
            {
                "position": position.name,
            } for position in positions
        ]

        return {"count": len(results), "positions": results}

    @doc(description=API_NAME, tags=API_TAGS)
    def post(self):
        if not request.is_json:
            return NOT_JSON_ERR_MSG

        data = request.get_json()
        new_pos = Position(
            name=data['name'],
        )
        db.session.add(new_pos)
        db.session.commit()
        return {"message": f"Position {new_pos.name} has been created successfully."}
