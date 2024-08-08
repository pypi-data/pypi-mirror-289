import unittest
from unittest.mock import patch
from src.samotpravil_smtp.client import SamotpravilClient
from src.samotpravil_smtp.exceptions import AuthorizationError, BadRequestError, StopListError, DomainNotTrustedError


class TestSamotpravilClient(unittest.TestCase):

    def setUp(self):
        self.client = SamotpravilClient(api_key='test_api_key')

    @patch('requests.post')
    def test_send_email_success(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "status": "OK",
            "message_id": "1qBv3w-0007Ls-CS"
        }

        response = self.client.send_email(
            email_to='test@example.com',
            subject='Test',
            message_text='This is a test email.',
            email_from='from@example.com'
        )
        self.assertEqual(response['status'], 'OK')

    @patch('requests.post')
    def test_send_email_authorization_error(self, mock_post):
        mock_post.return_value.status_code = 403
        mock_post.return_value.json.return_value = {
            "status": "error",
            "message": "Bad Api KEY, forbidden"
        }

        with self.assertRaises(AuthorizationError):
            self.client.send_email(
                email_to='test@example.com',
                subject='Test',
                message_text='This is a test email.',
                email_from='from@example.com'
            )

    @patch('requests.post')
    def test_send_email_bad_request_error(self, mock_post):
        mock_post.return_value.status_code = 400
        mock_post.return_value.json.return_value = {
            "status": "error",
            "message": "bad request send mail data"
        }

        with self.assertRaises(BadRequestError):
            self.client.send_email(
                email_to='test@example.com',
                subject='Test',
                message_text='This is a test email.',
                email_from='from@example.com'
            )

    @patch('requests.post')
    def test_send_email_stop_list_error(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "status": "error",
            "message": "error send mail: 550 bounced check filter"
        }

        with self.assertRaises(StopListError):
            self.client.send_email(
                email_to='test@example.com',
                subject='Test',
                message_text='This is a test email.',
                email_from='from@example.com'
            )

    @patch('requests.post')
    def test_send_email_domain_not_trusted_error(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "status": "error",
            "message": "error send mail: smtp error, cmd: close: 501 from domain not trusted"
        }

        with self.assertRaises(DomainNotTrustedError):
            self.client.send_email(
                email_to='test@example.com',
                subject='Test',
                message_text='This is a test email.',
                email_from='from@example.com'
            )


if __name__ == '__main__':
    unittest.main()
