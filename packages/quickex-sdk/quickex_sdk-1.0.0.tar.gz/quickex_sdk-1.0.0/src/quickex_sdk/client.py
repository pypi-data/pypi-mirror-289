import base64
import hashlib
import hmac
import json
import time

import requests

from src.quickex_sdk.models import Config


def create_signature(secret: str, message: str) -> bytes:
    hash = hmac.new(secret.encode('utf-8'), message.encode('utf-8'), hashlib.sha256)
    return base64.b64encode(hash.digest())


class Client:
    def __init__(self, config: Config):
        self.api_url = config.api_url
        self.api_public = config.api_public
        self.api_secret = config.api_secret
        self.session = requests.Session()
        self.session.base_url = config.api_url

    def post(self, url, body):
        timestamp = int(time.time())
        data_sign = f"{timestamp}{body}{self.api_public}"
        signature = create_signature(self.api_secret, data_sign).decode("utf-8")
        self.session.headers.update({'Accept': 'application/json'})
        self.session.headers.update({'Content-Type': 'application/json'})
        self.session.headers.update({'x-api-public-key': self.api_public})
        self.session.headers.update({'x-api-signature': signature})
        self.session.headers.update({'x-api-timestamp': timestamp.__str__()})
        return self.session.post(self.api_url + url, json=json.loads(body))

