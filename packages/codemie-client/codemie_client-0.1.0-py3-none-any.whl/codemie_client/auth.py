import requests

class KeycloakAuth:
    def __init__(self, server_url, client_id, client_secret, realm_name):
        self.server_url = server_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.realm_name = realm_name

    def get_token(self):
        url = f"{self.server_url}/auth/realms/{self.realm_name}/protocol/openid-connect/token"
        payload = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials'
        }

        response = requests.post(url, data=payload)
        response.raise_for_status()
        return response.json()['access_token']