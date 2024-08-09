import os

class SessionClient:
    BASE_URL = os.getenv("PERCULUS_XAPI_URL")

    def __init__(self, client):
        self.client = client

    def _make_request(self, method, endpoint, data=None, params=None):
        self.BASE_URL = f"https://{self.client.domain}/xapi" if self.client.domain is not None else self.BASE_URL
        url = f'{self.BASE_URL}/{endpoint}'
        return self.client._make_request(method, url, data=data, params=params)

    def list_sessions(self):
        return self._make_request("GET", 'session')
    
    def get_session(self, session_id):
        return self._make_request("GET", f'session/{session_id}')
    
    def create_session(self, payload):
        return self._make_request("POST", f'session', payload)
    
    def search_session(self, query):
        return self._make_request("GET", f'session', params=query)
    
    def update_session(self, session_id, payload):
        return self._make_request("PUT", f'session/{session_id}', payload)
    
    def delete_by_session_id(self, session_id):
        return self._make_request("DELETE", f'session/{session_id}')
    