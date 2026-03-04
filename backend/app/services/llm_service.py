import google.generativeai as genai
from app.config import settings

if settings.GEMINI_API_KEY:
    genai.configure(api_key=settings.GEMINI_API_KEY)
    # NOTE: the older client may not support newer model names reliably.
    # We keep the configured model but always fall back gracefully on errors.
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    model = None


def _fallback_answer(query: str, memories: list[str]) -> str:
    """
    Simple deterministic answer that does not rely on Gemini.
    Used when the model is unavailable or errors.
    """
    if not memories:
        return (
            f"I don't have any stored memories yet related to: '{query}'. "
            "Try adding some memories first, then ask again."
        )

    joined = "\n- ".join(memories[:5])
    return (
        "I couldn't reach the Gemini model right now, "
        "but here are the most relevant memories I found:\n\n"
        f"- {joined}\n\n"
        "Use these as context to answer your question."
    )


def generate_answer(query, memories):
    """
    Generate an answer using Gemini when possible.
    If Gemini is not configured or returns an error (404 / network / etc),
    return a safe, helpful fallback answer instead of raising 500.
    """
    if not model:
        return _fallback_answer(query, memories)

    context = "\n".join(memories) if memories else "(No relevant memories found)"
    prompt = f"""You are an AI personal memory assistant.

User Question:
{query}

Relevant Memories:
{context}

Use the memories to answer clearly. If no relevant memories were found, say so politely."""

    try:
        response = model.generate_content(prompt)
        # Some client versions return .text, others .candidates; be defensive.
        if hasattr(response, "text") and response.text:
            return response.text
        return _fallback_answer(query, memories)
    except Exception:
        # Any Gemini-related error should not crash the API.
        return _fallback_answer(query, memories)