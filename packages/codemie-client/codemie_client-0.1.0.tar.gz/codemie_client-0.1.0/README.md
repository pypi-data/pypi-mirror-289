# CodeMie Client

A Python client for interacting with the CodeMie API.

## Installation

```bash
poetry install codemie-client
```

## Usage

### Initialize CodeMie Client

```python
from codemie_client.client import CodeMieClient


client = CodeMieClient(
    auth_server_url="URL",
    auth_client_id="id",
    auth_client_secret="secret",
    auth_realm_name="codemie-dev",
    codemie_api_domain="https://URL/code-assistant-api"
)

token = client.get_token()
print(token)
```

### Retrieve Assistants

```python

token = "your_keycloak_token"
assistants = client.get_assistants(token=token)
print(assistants)
```

### Talk to Assistant

```python
from codemie_client.conversation import talk_to_assistant
from codemie_client.models import ChatRequest


token = "your_keycloak_token"
request = ChatRequest(
    assistant_id="ID",
    message="Hello!",
    history=[],
)
response_stream = client.talk_to_assistant_stream(request, token)
print(response)
```
