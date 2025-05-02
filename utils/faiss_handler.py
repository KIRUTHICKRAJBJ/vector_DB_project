
import faiss
import pickle
import os

INDEX_PATH = "faiss_index/faiss_index.index"
META_PATH = "faiss_index/faiss_index_meta.pkl"

def save_index(embeddings, chunks):
    index = faiss.IndexFlatL2(len(embeddings[0]))
    index.add(embeddings)
    os.makedirs("faiss_index", exist_ok=True)
    faiss.write_index(index, INDEX_PATH)
    with open(META_PATH, 'wb') as f:
        pickle.dump(chunks, f)

def search_index(query, model, k=5):
    index = faiss.read_index(INDEX_PATH)
    with open(META_PATH, 'rb') as f:
        chunks = pickle.load(f)
    query_vector = model.encode([query])
    _, I = index.search(query_vector, k)
    return [chunks[i] for i in I[0]]
    