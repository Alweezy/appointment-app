from api import database as db


class Doctor(db.Model):
    """This is the doctor model"""

    __tablename__ = 'doctors'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False, unique=True)
    last_name = db.Column(db.String(255), nullable=False, unique=True)
    appointments = db.relationship('Appointment', order_by="Appointment.id",
                                   cascade="all,delete-orphan")

    def __init__(self, first_name, last_name):
        """
        :param first_name: The doctor's first name
        :param last_name: The doctors second_name
        """

        self.first_name = first_name
        self.last_name = last_name

    def save(self):
        """Saves a doctor record into the database"""
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        """Fetches all the doctors from the database"""
        return Doctor.query.all()

    def delete(self):
        """Deletes an doctor with a particular id """
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return 'Doctor {}'.format(self.first_name, self.last_name)
