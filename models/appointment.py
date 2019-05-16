from api import database as db


class Appointment(db.Model):
    """This is the appointments model"""

    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    consultation_type = db.Column(db.String(255), nullable=False, unique=True)
    resolution = db.Column(db.String(255), nullable=False, unique=True)
    status = db.Column(db.String(255), nullable=False, unique=True)

    def __init__(self, venue, status, resolution, consultation_type):
        """
        :param venue: The place where the appointments is going to take place
        :param status: The status of the appointments, cancelled, confirmed, pending, resolved
        :param resolution: The outcome of the appointments
        :param status: The status of the appointments, could be cancelled, resolved, pending
        """

        self.venue = venue
        self.status = status
        self.resolution = resolution
        self.consultation_type = consultation_type

    def __repr__(self):
        return 'Doctor {}'.format(self.status)
