import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "backend"))

from fastapi.testclient import TestClient

try:
    from backend.app.main import app
except ModuleNotFoundError:
    from app.main import app


def test_health_check():
    with TestClient(app) as client:
        response = client.get("/health")
        assert response.status_code == 200
        body = response.json()
        assert body["status"] == "ok"
        assert body["vector_store_loaded"] is True
        assert body["chunk_count"] > 0


def test_query_happy_path():
    with TestClient(app) as client:
        response = client.post("/query", json={"question": "What does OBD-II code P0300 mean?"})
        assert response.status_code == 200
        body = response.json()
        assert "answer" in body
        assert isinstance(body["sources"], list)
        assert len(body["sources"]) > 0
        assert body["generation_mode"] in ("ollama", "fallback")


def test_query_invalid_input_returns_422():
    with TestClient(app) as client:
        # empty question violates min_length=1 on QueryRequest
        response = client.post("/query", json={"question": ""})
        assert response.status_code == 422


def test_query_missing_field_returns_422():
    with TestClient(app) as client:
        response = client.post("/query", json={})
        assert response.status_code == 422
        
# python -m pytest backend/tests/test_query.py -v