import unittest
from src.samotpravil_smtp.client import SamotpravilClient
from src.samotpravil_smtp.exceptions import SamotpravilError


class TestSamotpravilClient(unittest.TestCase):

    def setUp(self):
        self.client = SamotpravilClient(api_key='test_api_key')

    def test_send_email_success(self):
        # Mock the requests.post method to simulate a successful API response
        self.client._get_headers = lambda: {}
        self.client.send_email = lambda to, subject, body: {'status': 'success'}

        response = self.client.send_email('test@example.com', 'Test', 'This is a test email.')
        self.assertEqual(response['status'], 'success')

    def test_send_email_failure(self):
        # Mock the requests.post method to simulate a failed API response
        self.client._get_headers = lambda: {}
        self.client.send_email = lambda to, subject, body: self.assertRaises(SamotpravilError)

        with self.assertRaises(SamotpravilError):
            self.client.send_email('test@example.com', 'Test', 'This is a test email.')


if __name__ == '__main__':
    unittest.main()
