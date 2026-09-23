from typing import List, Optional
from pydantic import BaseModel, Field


class QueryRequest(BaseModel):
    question: str = Field(..., min_length=1, description="The user's natural-language question.")
    image_base64: Optional[str] = Field(
        default=None,
        description="Optional base64-encoded dashboard photo (Extended Track). "
        "If provided, YOLO detections are fused into the retrieval query.",
    )


class Detection(BaseModel):
    label: str
    confidence: float


class QueryResponse(BaseModel):
    answer: str
    sources: List[str]
    generation_mode: str
    detections: List[Detection] = []


class HealthResponse(BaseModel):
    status: str
    vector_store_loaded: bool
    chunk_count: int
    embedding_mode: str
    yolo_loaded: bool
