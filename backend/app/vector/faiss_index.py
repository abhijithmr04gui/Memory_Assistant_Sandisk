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
        if i < len(memory_store):
            results.append(memory_store[i])

    return results