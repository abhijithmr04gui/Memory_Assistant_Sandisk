from app.services.embedding_service import generate_embedding
from app.vector.faiss_index import search_vector

def retrieve_memories(query):

    query_vec = generate_embedding(query)

    results = search_vector(query_vec)

    return results