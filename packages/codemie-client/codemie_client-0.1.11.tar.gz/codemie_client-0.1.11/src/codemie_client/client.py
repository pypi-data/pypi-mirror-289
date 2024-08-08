from typing import List

from src.codemie_client.service.auth import KeycloakAuth
from .models import ChatRequest, GeneratedResponse, Assistant
from .service.assistants import AssistantsService


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
        self.assistants_service = AssistantsService(codemie_api_domain)

    def get_token(self):
        return self.auth_config.get_token()

    def exchange_user_token(self, user_email: str, token: str):
        return self.auth_config.exchange_token_for_user(user_email, token)

    def get_assistants(self, token: str) -> List[Assistant]:
        return self.assistants_service.get_assistants(token)

    def talk_to_assistant(self, request: ChatRequest, token: str) -> GeneratedResponse:
        return self.assistants_service.talk_to_assistant(request, token)

    def talk_to_assistant_stream(self, request: ChatRequest, token: str):
        return self.assistants_service.talk_to_assistant_stream(request, token)
