import os
from fastapi import FastAPI
from pydantic import BaseModel

from ai_agent_sample.agent.core import Agent
from ai_agent_sample.llm.mock import MockLLM
from ai_agent_sample.llm.bedrock import BedrockLLM
from dotenv import load_dotenv

load_dotenv()  # .env を読み込む

app = FastAPI()

use_mock = os.getenv("USE_MOCK", "0") == "1"
if use_mock:
    llm=MockLLM()
else:
    llm=BedrockLLM()

class ChatRequest(BaseModel):
    message: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/agent/chat")
def agent_chat(req: ChatRequest):
    agent = Agent(llm=llm)
    reply = agent.run(req.message)
    return {
        "reply": reply,
        "history_len": len(agent.history),
    }
