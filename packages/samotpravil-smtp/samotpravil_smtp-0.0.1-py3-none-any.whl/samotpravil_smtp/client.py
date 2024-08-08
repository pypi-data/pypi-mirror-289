import requests
from .exceptions import SamotpravilError


class SamotpravilClient:
    def __init__(self, api_key, base_url='https://api.samotpravil.ru'):
        self.api_key = api_key
        self.base_url = base_url

    def _get_headers(self):
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def send_email(self, to, subject, body):
        url = f"{self.base_url}/send"
        data = {
            'to': to,
            'subject': subject,
            'body': body
        }
        response = requests.post(url, json=data, headers=self._get_headers())
        if response.status_code != 200:
            raise SamotpravilError(response.json().get('message', 'Error sending email'))
        return response.json()
