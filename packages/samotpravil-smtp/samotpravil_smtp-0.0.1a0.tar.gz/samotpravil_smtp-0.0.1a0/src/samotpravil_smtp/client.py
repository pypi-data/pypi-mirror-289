import requests
from .exceptions import SamotpravilError, AuthorizationError, BadRequestError, StopListError, DomainNotTrustedError


class SamotpravilClient:
    def __init__(self, api_key, base_url='https://api.samotpravil.ru'):
        self.api_key = api_key
        self.base_url = base_url

    def _get_headers(self):
        return {
            'Authorization': self.api_key,
            'Content-Type': 'application/json'
        }

    def _handle_response(self, response):
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'OK':
                return data
            elif "550 bounced check filter" in data.get('message', ''):
                raise StopListError(data.get('message'))
            elif "from domain not trusted" in data.get('message', ''):
                raise DomainNotTrustedError(data.get('message'))
            else:
                raise SamotpravilError(data.get('message'))
        elif response.status_code == 403:
            raise AuthorizationError(response.json().get('message'))
        elif response.status_code == 400:
            raise BadRequestError(response.json().get('message'))
        else:
            response.raise_for_status()

    def send_email(self,
                   email_to: str,
                   subject: str,
                   message_text: str,
                   email_from: str,
                   name_from: str = None,
                   params: dict = None,
                   x_track_id: str = None,
                   track_open: bool = None,
                   track_click: bool = None,
                   track_domain: str = None,
                   check_stop_list: bool = None,
                   check_local_stop_list: bool = None,
                   domain_for_dkim: str = None,
                   headers: dict = None):

        url = f"{self.base_url}/api/v2/mail/send"

        if name_from:
            email_from = f"{name_from} <{email_from}>"

        data = {
            "email_from": email_from,
            "email_to": email_to,
            "subject": subject,
            "message_text": message_text,
            "params": params,
            "x_track_id": x_track_id,
            "track_open": track_open,
            "track_click": track_click,
            "track_domain": track_domain,
            "check_stop_list": check_stop_list,
            "check_local_stop_list": check_local_stop_list,
            "domain_for_dkim": domain_for_dkim,
            "headers": headers
        }

        data = {k: v for k, v in data.items() if v is not None}

        response = requests.post(url, json=data, headers=self._get_headers())
        return self._handle_response(response)
