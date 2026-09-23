import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # Vector store / RAG
    vector_store_dir: str = os.path.join(os.path.dirname(__file__), "..", "..", "data", "vector_store")
    collection_name: str = "automotive_docs"
    top_k: int = 4

    # LLM (Ollama)
    ollama_host: str = "http://localhost:11434"
    llm_model_name: str = "llama3.2:1b"

    # Vision (Extended Track)
    yolo_weights_path: str = os.path.join(
        os.path.dirname(__file__), "..", "..", "..", "data", "models", "dash_yolo_best.pt"
    )
    yolo_confidence_threshold: float = 0.5

    # CORS
    frontend_origin: str = "http://localhost:8501"


settings = Settings()
