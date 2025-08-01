import sys
import os
import unittest

# Add the 'app' directory to the Python path so we can import from app/app.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from app import app  # Now it will correctly import 'app' from 'app/app.py'

class TestApp(unittest.TestCase):
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Deployment Successful', response.data)

if __name__ == '__main__':
    unittest.main()
