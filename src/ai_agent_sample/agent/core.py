from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Protocol

Role = Literal["system", "user", "assistant"]


@dataclass
class Message:
    role: Role
    content: str


class LLMClient(Protocol):
    def chat(self, messages: List[Message]) -> str: ...


class Agent:
    def __init__(
        self, llm: LLMClient, system_prompt: str = "You are a helpful assistant."
    ):
        self._llm = llm
        self._history: List[Message] = [Message("system", system_prompt)]

    @property
    def history(self) -> List[Message]:
        return list(self._history)

    def run(self, user_input: str) -> str:
        self._history.append(Message("user", user_input))
        reply = self._llm.chat(self._history)
        self._history.append(Message("assistant", reply))
        return reply
