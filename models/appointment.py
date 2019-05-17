from api import database as db

from models.slot import Slot
from models.doctor import Doctor
from models.patient import Patient


class Appointment(db.Model):
    """This is the appointments model"""

    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    consultation_type = db.Column(db.String(255), nullable=False, unique=True)
    resolution = db.Column(db.String(255), nullable=False, unique=True)
    status = db.Column(db.String(255), nullable=False, unique=True)
    venue = db.Column(db.String(255), nullable=False, unique=True)
    date = db.Column(db.DateTime, default=db.func.current_timestamp())
    slot_id = db.Column(db.Integer, db.ForeignKey(Slot.id))

    doctor_id = db.Column(db.Integer, db.ForeignKey(Doctor.id))
    patient_id = db.Column(db.Integer, db.ForeignKey(Patient.id))

    def __init__(self, venue, status, resolution, consultation_type, slot_id, doctor_id, patient_id):
        """
        :param venue: The place where the appointments is going to take place
        :param status: The status of the appointments, cancelled, confirmed, pending, resolved
        :param resolution: The outcome of the appointments
        :param status: The status of the appointments, could be cancelled, resolved, pending
        :param slot_id: The window for which the appointment is scheduled
        :param doctor_id: The window for which the appointment is scheduled
        :param patient_id: The window for which the appointment is scheduled
        """

        self.venue = venue
        self.status = status
        self.resolution = resolution
        self.consultation_type = consultation_type
        self.slot_id = slot_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id

    def save(self):
        """Saves an appointment into the database"""
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        """Fetches all the appointments from the database"""
        return Appointment.query.all()

    def delete(self):
        """Deletes an appointment with a particular id """
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return 'Doctor {}'.format(self.status)
