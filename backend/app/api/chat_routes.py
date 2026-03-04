from fastapi import APIRouter, HTTPException
from app.services.retrieval_service import retrieve_memories
from app.services.llm_service import generate_answer

router = APIRouter()


@router.post("/chat")
def chat(data: dict):
    query = data.get("query", "").strip()
    if not query:
        raise HTTPException(status_code=400, detail="Query is required")
    memories = retrieve_memories(query)
    answer = generate_answer(query, memories)
    return {"answer": answer, "memories": memories}