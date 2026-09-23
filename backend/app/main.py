import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.routes.query import router as query_router
from app.services.retrieval import retrieval_service
from app.services.vision import vision_service
from app.utils.logging_config import configure_logging

configure_logging()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the vector store and models once at startup, not per-request.
    logger.info("Starting up: loading vector store and models...")
    retrieval_service.load()
    vision_service.load()  # non-fatal if unavailable; endpoint checks is_loaded
    logger.info("Startup complete.")
    yield
    logger.info("Shutting down.")


app = FastAPI(
    title="Automotive Diagnostics & Parts RAG Assistant",
    description="RAG-powered document assistant (Extended Track: RAG + YOLO vision) "
    "for automotive diagnostics and parts questions.",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.frontend_origin,
        "http://localhost:8501",
        "http://127.0.0.1:8501",
        "http://localhost:7860",
        "http://127.0.0.1:7860",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(query_router)


@app.get("/")
def root():
    return {"message": "Automotive RAG Assistant API. See /docs for the interactive API reference."}
