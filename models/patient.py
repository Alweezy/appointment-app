from api import database as db

from models.appointment import Appointment


class Patient(db.Model):
    """This is the patients model"""

    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False, unique=True)
    last_name = db.Column(db.String(255), nullable=False, unique=True)
    appointments = db.relationship('Appointment', order_by="Appointment.id",
                                   cascade="all,delete-orphan")

    def __init__(self, first_name, last_name):
        """
        :param first_name: patients's first name
        :param last_name: patients's second_name
        """
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return 'Patient {}'.format(self.first_name, self.last_name)
