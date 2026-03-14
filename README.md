# DocuMind

DocuMind is a **Retrieval-Augmented Generation (RAG) system** designed for intelligent document search and question answering.

The goal of this project is to understand and implement the **core mechanics of modern RAG pipelines** from scratch instead of relying entirely on frameworks.

DocuMind ingests documents, converts them into semantic embeddings, stores them in a vector index, and retrieves relevant context to answer user queries.

---

# Overview

Modern AI systems often struggle with **hallucination and outdated knowledge**.
RAG solves this by allowing language models to retrieve relevant information from external documents.

DocuMind implements the retrieval layer of a RAG system including:

* Document ingestion
* Token-aware chunking
* Embedding generation
* Vector indexing
* Semantic retrieval

---

# Architecture

The pipeline implemented in DocuMind:

```
Documents
   ↓
Document Loader
   ↓
Text Chunking
   ↓
Embedding Generation
   ↓
Vector Index (FAISS)
   ↓
Semantic Retrieval
   ↓
Relevant Context for LLM
```

This architecture mirrors the **retrieval pipeline used in production RAG systems**.

---

# Features

• Document ingestion from markdown files
• Token-aware chunking with configurable chunk size and overlap
• Local embedding generation using sentence-transformers
• FAISS vector index for semantic search
• Retrieval with similarity scoring
• Experimentation with chunking strategies

---

# Tech Stack

Python
FastAPI
FAISS (Vector Search)
Sentence Transformers (Embeddings)
Markdown document ingestion

---

# Project Structure

```
DocuMind
│
├── data/
│   └── raw_docs/            # source documents
│
├── src/
│   ├── loader.py            # document loader
│   ├── chunker.py           # chunking logic
│   ├── embedder.py          # embedding generation
│   └── vector_store.py      # FAISS vector search
│
├── run_rag.py               # retrieval pipeline
└── requirements.txt
```

---

# How It Works

1. Documents are loaded from the dataset directory.

2. Text is split into chunks using token-aware chunking with overlap to preserve context.

3. Each chunk is converted into a semantic embedding using a transformer model.

4. Embeddings are stored in a FAISS vector index.

5. User queries are embedded and compared against stored vectors to retrieve the most relevant chunks.

---

# Example Query

Example question:

```
How do background tasks work in FastAPI?
```

Retrieved output:

```
Source: background-tasks.md
Score: 0.63

You can define background tasks to be run after returning a response...
```

This demonstrates how semantic search retrieves relevant documentation.

---

# Future Improvements

Planned improvements include:

• Retrieval quality evaluation
• Chunk size experimentation
• Embedding model comparison
• RAG generation layer with LLM integration
• API interface for document querying

---

# Motivation

Many tutorials hide the complexity of RAG behind frameworks.

This project focuses on **building the retrieval pipeline manually** to gain a deeper understanding of:

* vector search
* embeddings
* chunking strategies
* retrieval quality

Understanding these components is essential for building **production-grade AI systems**.

---

# Author

Venkata Giridhar Reddy
AI Engineer focused on Generative AI and RAG systems
