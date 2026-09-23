import os
import base64
from typing import Optional

import requests

API_BASE_URL = os.environ.get("API_BASE_URL", "http://localhost:8000")


class ApiError(Exception):
    pass


def check_health() -> dict:
    resp = requests.get(f"{API_BASE_URL}/health", timeout=10)
    resp.raise_for_status()
    return resp.json()


def ask(question: str, image_bytes: Optional[bytes] = None) -> dict:
    payload = {"question": question}
    if image_bytes:
        payload["image_base64"] = base64.b64encode(image_bytes).decode("utf-8")

    try:
        resp = requests.post(f"{API_BASE_URL}/query", json=payload, timeout=60)
    except requests.exceptions.ConnectionError as e:
        raise ApiError(
            f"Could not reach the backend at {API_BASE_URL}. Is it running? ({e})"
        )

    if resp.status_code != 200:
        raise ApiError(f"Backend returned {resp.status_code}: {resp.text}")

    return resp.json()
