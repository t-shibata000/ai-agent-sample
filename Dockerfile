FROM python:3.11-slim

# Pythonの標準出力を即時flush（ログ用）
ENV PYTHONUNBUFFERED=1
# src-layout対応
ENV PYTHONPATH=/app/src

WORKDIR /app

# 依存関係（Poetry）
COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --only main

# アプリコード
COPY src ./src

# App RunnerはPORTを渡す
CMD ["sh", "-c", "uvicorn ai_agent_sample.main:app --host 0.0.0.0 --port ${PORT:-8080}"]
