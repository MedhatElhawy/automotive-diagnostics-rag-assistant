import logging
from typing import List, Dict, Any, Tuple

from app.core.config import settings

logger = logging.getLogger(__name__)

PROMPT_TEMPLATE = """You are an automotive diagnostics and parts assistant.
Answer the user's question using ONLY the context below. If the context
does not contain the answer, say you don't have enough information.
Cite the source document(s) you used in parentheses, e.g. (source: brake_system_diagnostics.md).

Context:
{context}

Question: {question}

Answer:"""


def build_prompt(question: str, hits: List[Dict[str, Any]]) -> str:
    context = "\n\n---\n\n".join(f"[{h['source']}]\n{h['text']}" for h in hits)
    return PROMPT_TEMPLATE.format(context=context, question=question)


def generate_answer(question: str, hits: List[Dict[str, Any]]) -> Tuple[str, str]:
    """Returns (answer, mode) where mode is 'ollama' or 'fallback'.

    Mirrors the notebook's generation strategy exactly: try a local Ollama
    server first; if it isn't reachable (e.g. not installed/running), fall
    back to a clearly-labeled extractive answer built from the top chunk so
    the API still returns a grounded, useful response.
    """
    if not hits:
        return "I don't have enough information in the knowledge base to answer that.", "fallback"

    prompt = build_prompt(question, hits)
    try:
        import ollama

        client = ollama.Client(host=settings.ollama_host)
        response = client.chat(
            model=settings.llm_model_name,
            messages=[{"role": "user", "content": prompt}],
        )
        return response["message"]["content"], "ollama"
    except Exception as e:
        logger.warning("Ollama unavailable (%s: %s); using extractive fallback.", type(e).__name__, e)
        top = hits[0]
        fallback = (
            f"[fallback mode - no Ollama server reachable] Based on the most relevant section: "
            f"{top['text'][:500].strip()} (source: {top['source']})"
        )
        return fallback, "fallback"
