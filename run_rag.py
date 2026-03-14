from src.loader import DocumentLoader
from src.chunker import TextChunker
from src.embedder import EmbeddingEngine
from src.vector_store import VectorStore


loader = DocumentLoader("data/raw_docs")
documents = loader.load_documents()

chunker = TextChunker(chunk_size=200, overlap=50)

all_chunks = []

for doc in documents:

    chunks = chunker.split_text(doc["text"])

    for chunk in chunks:
        all_chunks.append({
            "text": chunk,
            "source": doc["source"]
        })

print("Total documents:", len(documents))
print("Total chunks:", len(all_chunks))


embedder = EmbeddingEngine()

texts = [chunk["text"] for chunk in all_chunks]

embeddings = embedder.embed_batch(texts)

print("Embedding shape:", embeddings.shape)


# -------- VECTOR STORE --------

vector_store = VectorStore(dimension=384)

vector_store.add_embeddings(embeddings, all_chunks)

print("FAISS index built")


# -------- TEST QUERY --------

query = "How to create a fastapi app?"

query_embedding = embedder.embed_text(query)

results = vector_store.search(query_embedding, k=3)

print("\nQuery:", query)

print("\nTop Results:\n")

for i, r in enumerate(results, 1):

    print(f"Result {i}")
    print("Source:", r["source"])
    print("Score:", round(r["score"], 4))
    print(r["text"][:300])
    print("\n-----------------------------\n")