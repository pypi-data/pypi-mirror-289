import requests

class KeycloakAuth:
    def __init__(self, server_url, client_id, client_secret, realm_name):
        self.server_url = server_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.realm_name = realm_name

    def get_token(self):
        url = f"{self.server_url}/realms/{self.realm_name}/protocol/openid-connect/token"
        payload = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials'
        }

        response = requests.post(url, data=payload)
        response.raise_for_status()
        return response.json()['access_token']

    def exchange_token_for_user(self, email: str, access_token: str):
        user_id = self.find_user_by_email(email, access_token)
        return self._exchange_token_for_user(user_id, access_token)

    def find_user_by_email(self, email: str, access_token: str):
        url = f"{self.server_url}/admin/realms/{self.realm_name}/users?email={email}"
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        users = response.json()
        if not users:
            raise Exception("User not found")
        return users[0]['id']

    def _exchange_token_for_user(self, user_id, service_account_token):
        url = f"{self.server_url}/realms/{self.realm_name}/protocol/openid-connect/token"
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        payload = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'urn:ietf:params:oauth:grant-type:token-exchange',
            'subject_token': service_account_token,
            'requested_subject': user_id
        }

        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()

        return response.json()['access_token']