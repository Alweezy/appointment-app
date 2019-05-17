from flask import json

from tests.base import BaseTestCase


class AppointmentTestCases(BaseTestCase):
    def test_create_appointment(self):
        """Test for the successful creation of an appointment
        """

        self.client.post('/api/v1/doctors', data=json.dumps(self.doctor))
        self.client.post('/api/v1/patients', data=json.dumps(self.patient))
        self.client.post('/api/v1/slots', data=json.dumps(self.slot))
        response = self.client.post('/api/v1/appointments', data=json.dumps(self.appointment))

        self.assertEqual(response.status_code, 201)

    def test_get_appointments(self):
        """Test for the successful fetch of all the available appointments
        """
        self.client.post('/api/v1/doctors', data=json.dumps(self.doctor))
        self.client.post('/api/v1/patients', data=json.dumps(self.patient))
        self.client.post('/api/v1/slots', data=json.dumps(self.slot))

        self.client.post('/api/v1/appointments', data=json.dumps(self.appointment))

        response = self.client.get('/api/v1/appointments')

        self.assertEqual(response.status_code, 200)

    def test_get_appointment_by_id(self):
        """Test fot the successful fetch of a particular appointment
        """

        self.client.post('/api/v1/doctors', data=json.dumps(self.doctor))
        self.client.post('/api/v1/patients', data=json.dumps(self.patient))
        self.client.post('/api/v1/slots', data=json.dumps(self.slot))

        self.client.post('/api/v1/appointments', data=json.dumps(self.appointment))

        response = self.client.get('/api/v1/appointments/1')

        self.assertEqual(response.status_code, 200)

    def test_delete_appointment(self):
        """Test for the the successful delete of a particular appointment
        """
        self.client.post('/api/v1/doctors', data=json.dumps(self.doctor))
        self.client.post('/api/v1/patients', data=json.dumps(self.patient))
        self.client.post('/api/v1/slots', data=json.dumps(self.slot))

        self.client.post('/api/v1/appointments', data=json.dumps(self.appointment))

        response = self.client.delete('/api/v1/appointments/1')

        self.assertEqual(response.status_code, 204)

    def test_get_non_existent_appointment(self):
        """Test against the retrieval of a non existent appointment
        """
        self.client.post('/api/v1/doctors', data=json.dumps(self.doctor))
        self.client.post('/api/v1/patients', data=json.dumps(self.patient))
        self.client.post('/api/v1/slots', data=json.dumps(self.slot))

        self.client.post('/api/v1/appointments', data=json.dumps(self.appointment))

        self.client.delete('/api/v1/appointments/1')

        response = self.client.get('/api/v1/appointments/1')
        self.assertEqual(response.status_code, 404)

    def test_delete_non_existent_appointment(self):
        """Test against the delete of a non existent appointment
        """

        self.client.post('/api/v1/doctors', data=json.dumps(self.doctor))
        self.client.post('/api/v1/patients', data=json.dumps(self.patient))
        self.client.post('/api/v1/slots', data=json.dumps(self.slot))

        self.client.post('/api/v1/appointments', data=json.dumps(self.appointment))

        self.client.delete('/api/v1/appointments/1')

        response = self.client.get('/api/v1/appointments/1')

        self.assertEqual(response.status_code, 404)
