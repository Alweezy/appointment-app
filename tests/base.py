import unittest

from api import app, database as db


class BaseTestCase(unittest.TestCase):
    """Create the base for all tests
    """

    def setUp(self):
        """Initialize all the objects needed for testing
        """
        db.drop_all()
        db.create_all()

        self.doctor = {
            "doctor_id": "1",
            "first_name": "Khalifa",
            "last_name": "Blush"
        }

        self.patient = {
            "patient_id": "1",
            "first_name": "Noela",
            "last_name": "Imani"
        }

        self.slot = {
            "doctor_id": "1",
            "slot_id": "1",
            "start_time": "Thu, 16 May 2019 20:13:42 +0000",
            "end_time": "Thu, 16 May 2019 20:13:42 +0000"
        }

        self.appointment = {
                "appointment_id": "1",
                "consultation_type": "outpatient",
                "resolution": "come again",
                "status": "pending",
                "slot_id": "1",
                "venue": "Nairobi",
                "patient_id": "1",
                "doctor_id": "1"
            }

        self.client = app.test_client()

    def tearDown(self):
        """Clear database entries after every test
        """
        db.session.remove()
        db.drop_all()
