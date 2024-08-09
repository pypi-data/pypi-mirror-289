import os

class UserClient:
    BASE_URL = os.getenv("PERCULUS_XAPI_URL")

    def __init__(self, client):
        self.client = client

    def _make_request(self, method, endpoint, data=None, params=None):
        self.BASE_URL = f"https://{self.client.domain}/xapi" if self.client.domain is not None else self.BASE_URL
        url = f'{self.BASE_URL}/{endpoint}'
        return self.client._make_request(method, url, data=data, params=params)
    
    def create_user(self, payload):
        return self._make_request("POST", 'user', payload)
    
    def update_user(self, user_id, payload):
        return self._make_request("PUT", f'user/{user_id}', payload)
    
    def delete_by_user_id(self, user_id):
        return self._make_request("DELETE", f'user/{user_id}')
    
    def search_user(self, payload):
        return self._make_request("GET", f'user', data=payload)
    
    def get_user_by_id(self, user_id):
        return self._make_request("GET", f'user/{user_id}')
    
    def get_user_by_username(self, username):
        return self._make_request("GET", f'user/{username}')