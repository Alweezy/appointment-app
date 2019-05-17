from api import database as db


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
        :param first_name: patient's first name
        :param last_name: patient's second_name
        """
        self.first_name = first_name
        self.last_name = last_name

    def save(self):
        """Saves a patient record into the database"""
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        """Fetches all the patients from the database"""
        return Patient.query.all()

    def delete(self):
        """Deletes an patient with a particular id """
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return 'Patient {}'.format(self.first_name, self.last_name)
