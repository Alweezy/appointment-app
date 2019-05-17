from api import database as db

from models.doctor import Doctor


class Slot(db.Model):
    """This is the slots model"""

    __tablename__ = 'slots'

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, default=db.func.current_timestamp())
    end_time = db.Column(db.DateTime, default=db.func.current_timestamp())
    doctor_id = db.Column(db.Integer, db.ForeignKey(Doctor.id))
    slots = db.relationship('Appointment', order_by="Appointment.id",
                            cascade="all, delete-orphan", single_parent=True)

    def __init__(self, start_time, end_time, doctor_id):
        """
        :param start_time: The intended time to start an appointment
        :param end_time: The inteded time to end an appointment
        :param doctor_id: The doctor with whom the appointment is scheduled
        """

        self.start_time = start_time
        self.end_time = end_time
        self.doctor_id = doctor_id

    def save(self):
        """Saves a slot record into the database"""
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        """Fetches all the slots from the database"""
        return Slot.query.all()

    def delete(self):
        """Deletes an slot with a particular id """
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return 'Slot {}'.format(self.start_time, self.end_time)
