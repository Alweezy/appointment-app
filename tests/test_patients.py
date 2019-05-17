from flask import json

from tests.base import BaseTestCase


class AppointmentTestCases(BaseTestCase):
    def test_create_patient(self):
        """Test for the successful creation of a patient
        """

        response = self.client.post('/api/v1/patients', data=json.dumps(self.patient))

        self.assertEqual(response.status_code, 201)

    def test_get_patients(self):
        """Test for the successful fetch of all the available patient
        """
        self.client.post('/api/v1/patients', data=json.dumps(self.patient))
        response = self.client.get('/api/v1/patients')

        self.assertEqual(response.status_code, 200)

    def test_get_patient_by_id(self):
        """Test fot the successful fetch of a particular patient
        """

        self.client.post('/api/v1/patients', data=json.dumps(self.patient))
        response = self.client.get('/api/v1/patients')

        self.assertEqual(response.status_code, 200)

    def test_delete_patient(self):
        """Test for the the successful delete of a particular patient
        """
        self.client.post('/api/v1/patients', data=json.dumps(self.patient))

        response = self.client.delete('/api/v1/patients/1')

        self.assertEqual(response.status_code, 200)

    def test_get_non_existent_patient(self):
        """Test against the retrieval of a non existent patient
        """
        self.client.post('/api/v1/patients', data=json.dumps(self.patient))
        self.client.delete('/api/v1/patients/1')
        response = self.client.get('/api/v1/patients/1')

        self.assertEqual(response.status_code, 404)

    def test_delete_non_existent_patient(self):
        """Test against the delete of a non existent patient
        """

        self.client.post('/api/v1/patients', data=json.dumps(self.patient))

        self.client.delete('/api/v1/patients/1')

        response = self.client.get('/api/v1/patients/1')

        self.assertEqual(response.status_code, 404)
