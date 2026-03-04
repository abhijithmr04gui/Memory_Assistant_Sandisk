from fastapi import APIRouter, HTTPException
from app.services.memory_service import store_memory
from app.vector.faiss_index import memory_store

router = APIRouter()


@router.post("/memory")
def add_memory(data: dict):
    text = data.get("text", "").strip()
    if not text:
        raise HTTPException(status_code=400, detail="Text is required")
    return store_memory(text)


@router.get("/memories")
def get_memories():
    """Return all stored memories for timeline display."""
    return [{"text": m, "timestamp": None} for m in memory_store]