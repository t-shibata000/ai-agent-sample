import os

from dotenv import load_dotenv

load_dotenv()

print("AWS_ACCESS_KEY_ID set:", bool(os.getenv("AWS_ACCESS_KEY_ID")))
print("BEDROCK_REGION:", os.getenv("BEDROCK_REGION"))
print("BEDROCK_MODEL_ID:", os.getenv("BEDROCK_MODEL_ID"))
