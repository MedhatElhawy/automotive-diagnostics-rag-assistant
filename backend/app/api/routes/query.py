import logging

from fastapi import APIRouter, HTTPException

from app.schemas.query import QueryRequest, QueryResponse, HealthResponse, Detection
from app.services.retrieval import retrieval_service
from app.services.generation import generate_answer
from app.services.vision import vision_service

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(
        status="ok",
        vector_store_loaded=retrieval_service.is_loaded,
        chunk_count=retrieval_service.chunk_count,
        embedding_mode=retrieval_service.embedding_mode,
        yolo_loaded=vision_service.is_loaded,
    )


@router.post("/query", response_model=QueryResponse)
def query(request: QueryRequest) -> QueryResponse:
    if not retrieval_service.is_loaded:
        raise HTTPException(status_code=503, detail="Vector store is not loaded yet.")

    question = request.question
    detections: list = []

    # Extended Track: fuse image detections into the retrieval query
    if request.image_base64:
        if not vision_service.is_loaded:
            raise HTTPException(status_code=503, detail="Vision model is not available on this server.")
        try:
            raw_detections = vision_service.detect(request.image_base64)
        except Exception as e:
            raise HTTPException(status_code=422, detail=f"Could not process image: {e}")

        detections = [Detection(label=label, confidence=round(conf, 3)) for label, conf in raw_detections]
        prefix = vision_service.detections_to_query_prefix(raw_detections)
        if prefix:
            question = f"{prefix}{question}"

    hits = retrieval_service.retrieve(question)
    answer, mode = generate_answer(question, hits)
    sources = sorted({h["source"] for h in hits})

    return QueryResponse(answer=answer, sources=sources, generation_mode=mode, detections=detections)
