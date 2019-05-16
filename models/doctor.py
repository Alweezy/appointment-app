from api import database as db

from models.appointment import Appointment


class Doctor(db.Model):
    """This is the doctor model"""

    __tablename__ = 'doctors'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False, unique=True)
    last_name = db.Column(db.String(255), nullable=False, unique=True)
    available = db.Column(db.String(255), nullable=False)
    appointments = db.relationship('Appointment', order_by="Appointment.id",
                                   cascade="all,delete-orphan")

    def __init__(self, first_name, last_name, available):
        """
        :param first_name: The doctor's first name
        :param last_name: The doctors second_name
        :param available: Boolean value indicating doctor's availability
        """

        self.first_name = first_name
        self.last_name = last_name
        self.available = available

    def __repr__(self):
        return 'Doctor {}'.format(self.first_name, self.last_name)
