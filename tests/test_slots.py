from flask import json

from tests.base import BaseTestCase


class AppointmentTestCases(BaseTestCase):
    def test_create_slot(self):
        """Test for the successful creation of a slot
        """

        self.client.post('/api/v1/doctors', data=json.dumps(self.doctor))
        response = self.client.post('/api/v1/slots', data=json.dumps(self.slot))

        self.assertEqual(response.status_code, 201)

    def test_get_slots(self):
        """Test for the successful fetch of all the available slot
        """

        self.client.post('/api/v1/doctors', data=json.dumps(self.doctor))
        self.client.post('/api/v1/slots', data=json.dumps(self.slot))
        response = self.client.get('/api/v1/slots')

        self.assertEqual(response.status_code, 200)

    def test_get_slot_by_id(self):
        """Test fot the successful fetch of a particular slot
        """

        self.client.post('/api/v1/doctors', data=json.dumps(self.doctor))
        self.client.post('/api/v1/slots', data=json.dumps(self.slot))
        response = self.client.get('/api/v1/slots')

        self.assertEqual(response.status_code, 200)

    def test_delete_slot(self):
        """Test for the the successful delete of a particular slot
        """
        self.client.post('/api/v1/doctors', data=json.dumps(self.doctor))
        self.client.post('/api/v1/slots', data=json.dumps(self.slot))

        response = self.client.delete('/api/v1/slots/1')

        self.assertEqual(response.status_code, 200)

    def test_get_non_existent_slot(self):
        """Test against the retrieval of a non existent slot
        """

        self.client.post('/api/v1/doctors', data=json.dumps(self.doctor))
        self.client.post('/api/v1/slots', data=json.dumps(self.slot))
        self.client.delete('/api/v1/slots/1')
        response = self.client.get('/api/v1/slots/1')

        self.assertEqual(response.status_code, 404)

    def test_delete_non_existent_slot(self):
        """Test against the delete of a non existent slot
        """

        self.client.post('/api/v1/doctors', data=json.dumps(self.doctor))
        self.client.post('/api/v1/slots', data=json.dumps(self.slot))

        self.client.delete('/api/v1/slots/1')

        response = self.client.get('/api/v1/slots/1')

        self.assertEqual(response.status_code, 404)
