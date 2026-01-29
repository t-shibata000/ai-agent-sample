import os
import json
from typing import List

import boto3
from botocore.exceptions import ClientError

from ai_agent_sample.agent.core import Message
from dotenv import load_dotenv

load_dotenv()  # .env を読み込む

class BedrockLLM:
    def __init__(self):
        self._region = os.getenv("BEDROCK_REGION", "ap-northeast-1")
        self._model_id = os.getenv(
            "BEDROCK_MODEL_ID", 
            "anthropic.claude-3-haiku-20240307-v1:0"
        )
        self._client = boto3.client(
            "bedrock-runtime",
            region_name=self._region,
        )

    def chat(self, messages: List[Message]) -> str:
        # 1. Message → Bedrock形式
        bedrock_messages = [
            {
                "role": m.role,
                "content": [{"type": "text", "text": m.content}],
            }
            for m in messages
            if m.role != "system"
        ]

        system_prompt = next(
            (m.content for m in messages if m.role == "system"),
            "",
        )

        body = {
            "anthropic_version": "bedrock-2023-05-31",
            "system": system_prompt,
            "messages": bedrock_messages,
            "max_tokens": 256,
            "temperature": 0.7,
        }
        try:
            # 2. invoke_model
            response = self._client.invoke_model(
                modelId=self._model_id,
                body=json.dumps(body),
                contentType="application/json",
                accept="application/json",
            )
        except ClientError as e:
            # 最低限、原因が分かるようにする
            raise RuntimeError(
                f"Bedrock invoke_model failed: {e.response.get('Error', {}).get('Code')} "
                f"{e.response.get('Error', {}).get('Message')}"
            ) from e         

        # 3. レスポンス解析
        payload = json.loads(response["body"].read().decode("utf-8"))
        return payload["content"][0]["text"]
