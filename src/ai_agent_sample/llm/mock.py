from typing import List

from ai_agent_sample.agent.core import Message


class MockLLM:
    def chat(self, messages: List[Message]) -> str:
        last_user = next(
            (m.content for m in reversed(messages) if m.role == "user"), ""
        )
        return f"[mock] you said: {last_user}"
