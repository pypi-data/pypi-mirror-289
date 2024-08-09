import os
import requests

class AuthClient:
    def __init__(self):
        self.base_url = os.getenv("PERCULUS_AUTH_URL")

    def authenticate(self, access_key, secret_key, account_id, domain=None):
        self.base_url = f"https://{domain}/auth" if domain is not None else self.base_url
        url = f"{self.base_url}/connect/token"
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        data = {
            "username": access_key, 
            "password": secret_key, 
            "account_id": account_id, 
            "client_id": "api", 
            "grant_type": "password"
        }

        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()
        return response.json()