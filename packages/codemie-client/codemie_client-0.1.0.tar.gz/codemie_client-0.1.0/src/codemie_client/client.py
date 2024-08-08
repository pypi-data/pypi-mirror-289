import json
from typing import List

import requests

from .auth import KeycloakAuth
from .models import ChatRequest, ChatResponse, GeneratedResponse, Assistant


class CodeMieClient:
    def __init__(self,
                 auth_server_url: str,
                 auth_client_id: str,
                 auth_client_secret: str,
                 auth_realm_name: str,
                 codemie_api_domain: str):
        self.auth_server_url = auth_server_url
        self.auth_client_id = auth_client_id
        self.auth_client_secret = auth_client_secret
        self.auth_realm_name = auth_realm_name
        self.codemie_api_domain = codemie_api_domain

        # Initialize Keycloak Authentication
        self.auth_config = KeycloakAuth(
            server_url=auth_server_url,
            client_id=auth_client_id,
            client_secret=auth_client_secret,
            realm_name=auth_realm_name
        )

    def get_token(self):
        return self.auth_config.get_token()

    def get_assistants(self, token: str) -> List[Assistant]:
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response = requests.get(f'{self.codemie_api_domain}/v1/assistants', headers=headers)
        response.raise_for_status()
        assistants_data = response.json()
        return [Assistant(**assistant) for assistant in assistants_data]

    def talk_to_assistant(self, request: ChatRequest, token: str) -> GeneratedResponse:
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        data = {
            'text': request.message,
            'history': request.history,
            'stream': False,
        }
        response = requests.post(url=f'{self.codemie_api_domain}/v1/assistants/{request.assistant_id}/model',
                                 headers=headers,
                                 json=data)
        final_response = response.json()
        return GeneratedResponse.from_dict(final_response)

    def talk_to_assistant_stream(self, request: ChatRequest, token: str):
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        data = {
            'text': request.message,
            'history': request.history,
            'stream': True,
        }

        response = requests.post(url=f'{self.codemie_api_domain}/v1/assistants/{request.assistant_id}/model',
                                 headers=headers,
                                 json=data,
                                 stream=True)
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                yield ChatResponse.from_dict(json.loads(chunk.decode('utf-8')))
