import json
import os

import boto3
from dotenv import load_dotenv

load_dotenv()  # .env を読み込む


def _bedrock_client():
    # Bedrockのモデルが有効なリージョンを指定（例： us-east-1）
    region = os.getenv("BEDROCK_REGION", "us-east-1")
    return boto3.client("bedrock-runtime", region_name=region)


def call_claude(prompt: str, max_tokens: int = 256) -> str:
    """
    Claude (Bedrock) を1回呼び出してテキストを返す
    """
    model_id = os.getenv("BEDROCK_MODEL_ID", "anthropic.claude-3-haiku-20240307-v1:0")

    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": prompt}],
    }

    client = _bedrock_client()
    response = client.invoke_model(
        modelId=model_id,
        body=json.dumps(body),
        contentType="application/json",
        accept="application/json",
    )

    data = json.loads(response["body"].read())
    return data["content"][0]["text"]
