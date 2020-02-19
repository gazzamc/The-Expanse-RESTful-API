import unittest
import json
from routes import app


class PeopleTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_api_people_response(self):
        rv = self.app.get('/api/people', follow_redirects=True)
        self.assertEqual(rv.status, '200 OK')

    def test_api_people_valid_record(self):
        rv = self.app.get('/api/people/1')
        self.get_json = json.loads(rv.data)
        self.assertEqual(self.get_json['data']['name'], 'Captain McDowell')

    def test_api_people_invalid_record(self):
        rv = self.app.get('/api/people/2')
        self.get_json = json.loads(rv.data)
        self.assertEqual(self.get_json['message'], 'Record does not exist')

    def test_api_people_invalid_id(self):
        rv = self.app.get('/api/people/james')
        self.get_json = json.loads(rv.data)
        self.assertEqual(self.get_json['message'], 'Bad Request. ID must be an integer')


if __name__ == '__main__':
    unittest.main()
