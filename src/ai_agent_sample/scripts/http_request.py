# tools/test_agent.py
import httpx

resp = httpx.post(
    "http://127.0.0.1:8000/agent/chat",
    json={"message": "こんにちは"},
    timeout=10,
)

print(resp.status_code)
print(resp.text)
