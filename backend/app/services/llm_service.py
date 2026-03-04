import google.generativeai as genai
from app.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_answer(query, memories):

    context = "\n".join(memories)

    prompt = f"""
You are an AI personal memory assistant.

User Question:
{query}

Relevant Memories:
{context}

Use the memories to answer clearly.
"""

    response = model.generate_content(prompt)

    return response.text