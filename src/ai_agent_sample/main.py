from fastapi import FastAPI
from pydantic import BaseModel

from ai_agent_sample.agent.core import Agent
from ai_agent_sample.llm.mock import MockLLM

app = FastAPI()

agent = Agent(llm=MockLLM())


class ChatRequest(BaseModel):
    message: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/agent/chat")
def agent_chat(req: ChatRequest):
    reply = agent.run(req.message)
    return {
        "reply": reply,
        "history_len": len(agent.history),
    }
