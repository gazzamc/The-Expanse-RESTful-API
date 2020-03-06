import unittest
import json
from routes import app


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_api_people_response(self):
        rv = self.app.get('/api/people', follow_redirects=True)
        self.assertEqual(rv.status, '200 OK')

    def test_api_locations_response(self):
        rv = self.app.get('/api/locations', follow_redirects=True)
        self.assertEqual(rv.status, '200 OK')

    def test_api_systems_response(self):
        rv = self.app.get('/api/systems', follow_redirects=True)
        self.assertEqual(rv.status, '200 OK')

    def test_api_people_valid_record(self):
        rv = self.app.get('/api/people/1')
        self.get_json = json.loads(rv.data)
        self.assertEqual(self.get_json['data']['name'], 'Captain McDowell')

    def test_api_locations_valid_record(self):
        rv = self.app.get('/api/locations/1')
        self.get_json = json.loads(rv.data)
        self.assertEqual(self.get_json['data']['name'], 'earth')

    def test_api_systems_valid_record(self):
        rv = self.app.get('/api/systems/1')
        self.get_json = json.loads(rv.data)
        self.assertEqual(self.get_json['data']['name'], 'sol')

    def test_api_people_invalid_record(self):
        rv = self.app.get('/api/people/2')
        self.get_json = json.loads(rv.data)
        self.assertEqual(self.get_json['message'], 'Record does not exist')

    def test_api_locations_invalid_record(self):
        rv = self.app.get('/api/locations/2')
        self.get_json = json.loads(rv.data)
        self.assertEqual(self.get_json['message'], 'Record does not exist')

    def test_api_systems_invalid_record(self):
        rv = self.app.get('/api/systems/2')
        self.get_json = json.loads(rv.data)
        self.assertEqual(self.get_json['message'], 'Record does not exist')

    def test_api_people_invalid_id(self):
        rv = self.app.get('/api/people/james')
        self.get_json = json.loads(rv.data)
        self.assertEqual(
            self.get_json['message'], 'Bad Request. ID must be an integer')

    def test_api_locations_invalid_id(self):
        rv = self.app.get('/api/locations/test')
        self.get_json = json.loads(rv.data)
        self.assertEqual(
            self.get_json['message'], 'Bad Request. ID must be an integer')

    def test_api_systems_invalid_id(self):
        rv = self.app.get('/api/systems/test')
        self.get_json = json.loads(rv.data)
        self.assertEqual(
            self.get_json['message'], 'Bad Request. ID must be an integer')

    def test_api_invalid_endpoint(self):
        rv = self.app.get('/api/newEndPoint')
        self.get_json = json.loads(rv.data)
        self.assertEqual(
            self.get_json['message'], 'Invalid EndPoint')

    def test_api_invalid_URI(self):
        rv = self.app.get('/api/people?testquery=test')
        self.get_json = json.loads(rv.data)
        self.assertEqual(
            self.get_json['message'], 'Bad Request. Query string unrecognised')


if __name__ == '__main__':
    unittest.main()
