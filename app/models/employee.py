from app import db


class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    position = db.Column(
        db.Integer,
        db.ForeignKey('positions.id', onupdate='CASCADE', ondelete='CASCADE'),
        nullable=False
    )

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f'{self.surname} {self.name}'
