from app.services.embedding_service import generate_embedding
from app.vector.faiss_index import add_vector

def store_memory(text):

    embedding = generate_embedding(text)

    add_vector(embedding, text)

    return {"status": "memory stored"}