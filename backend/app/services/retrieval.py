import json
import logging
import os
from typing import List, Dict, Any

import chromadb
import joblib

from app.core.config import settings

logger = logging.getLogger(__name__)


class RetrievalService:
    """Loads the persisted Chroma vector store (built by notebooks/rag_pipeline.ipynb)
    once at startup and serves retrieval queries. Mirrors the exact embedding
    strategy used at index time (sentence-transformers, or a TF-IDF fallback),
    read from the exported config.json so encoding stays consistent.
    """

    def __init__(self) -> None:
        self.client = None
        self.collection = None
        self.config: Dict[str, Any] = {}
        self.embedding_mode = "uninitialized"
        self._st_model = None
        self._tfidf_vectorizer = None

    def load(self) -> None:
        config_path = os.path.join(settings.vector_store_dir, "config.json")
        if not os.path.exists(config_path):
            raise RuntimeError(
                f"No vector store config found at {config_path}. "
                "Run notebooks/rag_pipeline.ipynb first to build and export the vector store."
            )
        with open(config_path) as f:
            self.config = json.load(f)

        self.client = chromadb.PersistentClient(path=settings.vector_store_dir)
        self.collection = self.client.get_collection(name=self.config.get("collection_name", settings.collection_name))
        self.embedding_mode = self.config["embedding_mode"]

        if self.embedding_mode == "sentence-transformers":
            from sentence_transformers import SentenceTransformer
            self._st_model = SentenceTransformer(self.config["embedding_model_name"])
        elif self.embedding_mode == "tfidf":
            vec_path = self.config.get("tfidf_vectorizer_path")
            if not vec_path or not os.path.exists(vec_path):
                raise RuntimeError("TF-IDF fallback mode but no persisted vectorizer found.")
            self._tfidf_vectorizer = joblib.load(vec_path)
        else:
            raise RuntimeError(f"Unknown embedding_mode in config.json: {self.embedding_mode}")

        logger.info(
            "Vector store loaded: %d chunks, embedding_mode=%s",
            self.collection.count(),
            self.embedding_mode,
        )

    @property
    def is_loaded(self) -> bool:
        return self.collection is not None

    @property
    def chunk_count(self) -> int:
        return self.collection.count() if self.collection else 0

    def _embed_query(self, text: str) -> List[float]:
        if self.embedding_mode == "sentence-transformers":
            return self._st_model.encode([text], show_progress_bar=False)[0].tolist()
        else:
            return self._tfidf_vectorizer.transform([text]).toarray()[0].tolist()

    def retrieve(self, question: str, k: int = None) -> List[Dict[str, Any]]:
        if not self.is_loaded:
            raise RuntimeError("RetrievalService.load() must be called before retrieve().")
        k = k or self.config.get("top_k", settings.top_k)
        query_embedding = self._embed_query(question)
        results = self.collection.query(query_embeddings=[query_embedding], n_results=k)

        hits = []
        docs = results.get("documents", [[]])[0]
        metas = results.get("metadatas", [[]])[0]
        dists = results.get("distances", [[]])[0]
        for doc, meta, dist in zip(docs, metas, dists):
            hits.append({"text": doc, "source": meta.get("source", "unknown"), "distance": dist})
        return hits


# module-level singleton, created once and reused across requests
retrieval_service = RetrievalService()
