from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class ChatRole(str, Enum):
    ASSISTANT = "Assistant"
    USER = "User"


class ChatMessage(BaseModel):
    role: ChatRole
    message: str


class ChatRequest(BaseModel):
    assistant_id: str
    message: str
    history: list[ChatMessage]


@dataclass
class Thought:
    id_: str
    in_progress: bool
    tool_name: str
    message: str


@dataclass
class ChatResponse:
    time_elapsed: Optional[float]
    input_tokens_used: Optional[int]
    tokens_used: int
    generated_chunk: Optional[str]
    generated: Optional[str]
    thought: Thought
    last: bool
    debug: Optional[str]

    @staticmethod
    def from_dict(data: dict) -> 'ChatResponse':
        thought_data = data.get('thought', {})
        if thought_data:
            thought = Thought(
                id_=thought_data.get('id_', ''),
                in_progress=thought_data.get('in_progress', False),
                tool_name=thought_data.get('tool_name', ''),
                message=thought_data.get('message', '')
            )
        else:
            thought = None
        return ChatResponse(
            time_elapsed=data.get('time_elapsed'),
            input_tokens_used=data.get('input_tokens_used'),
            tokens_used=data.get('tokens_used', 0),
            generated_chunk=data.get('generated_chunk'),
            generated=data.get('generated'),
            thought=thought,
            last=data.get('last', False),
            debug=data.get('debug')
        )


class GeneratedResponse(BaseModel):
    generated: Optional[str]
    timeElapsed: Optional[float]
    tokensUsed: Optional[int]
    taskId: Optional[str]

    @staticmethod
    def from_dict(data: dict) -> 'GeneratedResponse':
        return GeneratedResponse(
            generated=data.get("generated"),
            timeElapsed=data.get("time_elapsed"),
            tokensUsed=data.get("tokens_used"),
            taskId=data.get("task_id")
        )

class CreatedBy(BaseModel):
    id: Optional[str]
    username: Optional[str]
    name: Optional[str]


class Tool(BaseModel):
    name: str
    label: str
    settings_config: bool
    settings: Optional[dict]


class Toolkit(BaseModel):
    toolkit: str
    tools: List[Tool]
    label: str
    settings_config: bool
    settings: Optional[dict]


class Context(BaseModel):
    context_type: str
    name: str


class Assistant(BaseModel):
    id: str
    appVersion: str
    kbVersion: Optional[str]
    date: str
    update_date: Optional[str]
    name: str
    description: str
    system_prompt: str
    created_by: CreatedBy
    project: str
    icon_url: Optional[str]
    llm_model_type: str
    toolkits: List[Toolkit]
    shared: bool
    is_react: bool
    is_global: bool
    created_date: str
    updated_date: Optional[str]
    agent_mode: str
    plan_prompt: Optional[str]
    creator: str
    slug: Optional[str]
    context: List[Context]
    user_abilities: List[str]
