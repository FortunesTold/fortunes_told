import unittest
import os
from server import app

key = os.environ['FLASK_SECRET']

class FlaskTests(unittest.TestCase):
    def setUp(self):
        """Set up before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_home_page_is_ok(self):
        """Testing initial homepage."""

        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)

    def test_homepage_contains_hello(self):
        result = self.client.get('/')
        self.assertIn('Hello', result.data)

    def test_homepage_contains_hacktober(self):
        result = self.client.get('/')
        self.assertIn('Hacktober', result.data)

    def test_fortunes_page_is_ok(self):
        result = self.client.get('/fortunes')
        self.assertEqual(result.status_code, 200)

    def test_fortunes_is_not_empty(self):
        result = self.client.get('/fortunes')
        self.assertNotEqual('<html><body></body></html>', result.data)






###################
if __name__ == '__main__':
    unittest.main()