from flask import json

from tests.base import BaseTestCase


class AppointmentTestCases(BaseTestCase):
    def test_create_doctor(self):
        """Test for the successful creation of a doctor
        """

        response = self.client.post('/api/v1/doctors', data=json.dumps(self.doctor))

        self.assertEqual(response.status_code, 201)

    def test_get_doctors(self):
        """Test for the successful fetch of all the available doctors
        """
        self.client.post('/api/v1/doctors', data=json.dumps(self.doctor))
        response = self.client.get('/api/v1/doctors')

        self.assertEqual(response.status_code, 200)

    def test_get_doctor_by_id(self):
        """Test fot the successful fetch of a particular doctor
        """

        self.client.post('/api/v1/doctors', data=json.dumps(self.doctor))
        response = self.client.get('/api/v1/doctors')

        self.assertEqual(response.status_code, 200)

    def test_delete_doctor(self):
        """Test for the the successful delete of a particular doctor
        """
        self.client.post('/api/v1/doctors', data=json.dumps(self.doctor))

        response = self.client.delete('/api/v1/doctors/1')

        self.assertEqual(response.status_code, 200)

    def test_get_non_existent_doctor(self):
        """Test against the retrieval of a non existent doctor
        """
        self.client.post('/api/v1/doctors', data=json.dumps(self.doctor))
        self.client.delete('/api/v1/doctors/1')
        response = self.client.get('/api/v1/doctors/1')

        self.assertEqual(response.status_code, 404)

    def test_delete_non_existent_doctor(self):
        """Test against the delete of a non existent doctor
        """

        self.client.post('/api/v1/doctors', data=json.dumps(self.doctor))

        self.client.delete('/api/v1/doctors/1')

        response = self.client.get('/api/v1/appointments/1')

        self.assertEqual(response.status_code, 404)
