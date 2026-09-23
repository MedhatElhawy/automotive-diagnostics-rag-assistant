FROM python:3.12-slim

WORKDIR /app

# System deps needed by opencv/ultralytics at runtime
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY data ./data

# The YOLO weights and the notebook-built vector store are expected to be
# present under ./data (vector_store/) and ../data/models (mounted or
# copied in) — see the README for how to build/copy them before deploying.

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
