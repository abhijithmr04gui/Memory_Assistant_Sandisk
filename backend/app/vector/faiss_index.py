import faiss
import numpy as np

dimension = 384

index = faiss.IndexFlatL2(dimension)

memory_store = []

def add_vector(vector, memory_text):

    vec = np.array([vector]).astype("float32")

    index.add(vec)

    memory_store.append(memory_text)


def search_vector(vector, k=5):

    vec = np.array([vector]).astype("float32")

    distances, indices = index.search(vec, k)

    results = []

    for i in indices[0]:
        # FAISS returns -1 when k > ntotal or no valid result
        if 0 <= i < len(memory_store):
            results.append(memory_store[i])

    return results