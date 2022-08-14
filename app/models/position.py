from app import db


class Position(db.Model):
    __tablename__ = 'positions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)  # TODO criteria clarification is required

    def __init__(self, name):
        self.name = name
