import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    PROJECT_NAME = "Memory OS"

    # Gemini API key from .env
    GEMINI_API_KEY = os.getenv("AIzaSyB6hD5q4k-GxrttHjXgEAAzGK97nfNW5No")

    # Embedding model
    EMBEDDING_MODEL = "all-MiniLM-L6-v2"

    # FAISS vector dimension
    VECTOR_DIMENSION = 384

    # Retrieval results
    TOP_K_RESULTS = 5


settings = Settings()