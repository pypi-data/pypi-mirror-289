import json
from typing import List

import requests

from src.codemie_client.models import Assistant, ChatRequest, GeneratedResponse, ChatResponse


class AssistantsService:
    CHUNK_SIZE = 8192

    def __init__(self, codemie_base_url):
        self.codemie_base_url = codemie_base_url

    def get_assistants(self, token: str) -> List[Assistant]:
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response = requests.get(f'{self.codemie_base_url}/v1/assistants', headers=headers)
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
        response = requests.post(url=f'{self.codemie_base_url}/v1/assistants/{request.assistant_id}/model',
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

        response = requests.post(url=f'{self.codemie_base_url}/v1/assistants/{request.assistant_id}/model',
                                 headers=headers,
                                 json=data,
                                 stream=True)
        for chunk in response.iter_content(chunk_size=self.CHUNK_SIZE):
            if chunk:
                yield ChatResponse.from_dict(json.loads(chunk.decode('utf-8')))
