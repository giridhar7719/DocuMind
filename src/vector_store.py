import faiss
import numpy as np


class VectorStore:

    def __init__(self, dimension):

        self.index = faiss.IndexFlatL2(dimension)
        self.data = []

    def add_embeddings(self, embeddings, chunks):

        embeddings = np.array(embeddings).astype("float32")

        self.index.add(embeddings)

        self.data.extend(chunks)

    def search(self, query_embedding, k=5):

        query_embedding = np.array([query_embedding]).astype("float32")

        distances, indices = self.index.search(query_embedding, k)

        results = []

        for i, idx in enumerate(indices[0]):

            chunk_data = self.data[idx]

            results.append({
                "text": chunk_data["text"],
                "source": chunk_data["source"],
                "score": float(distances[0][i])
            })

        return results