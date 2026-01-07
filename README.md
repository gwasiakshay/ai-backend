AI Backend – Retrieval-Augmented Generation (RAG)

A production-style AI backend implementing a complete Retrieval-Augmented Generation (RAG) pipeline with clean architecture, async processing, and persistent memory.

Status: Step 4 (RAG) complete and intentionally frozen.

🚀 What This Demonstrates

This project proves the ability to:

Design end-to-end AI systems, not just call LLM APIs

Build production-grade backends using FastAPI

Implement correct RAG (retrieval → grounding → generation)

Separate semantic memory from system state

Integrate LLM providers safely and debuggably

Operate async pipelines with background workers

🧠 System Overview

Flow

Document → Chunking → Embeddings → Vector DB → Retrieval → Context → LLM Answer


Key Design Choices

Thin API routes, logic in services

Async ingestion via background worker

Vector DB for semantic search

Relational DB for metadata & job state

Provider-agnostic LLM abstraction

🏗️ Tech Stack

FastAPI – API layer

Background Worker – async ingestion

Chroma – vector database

PostgreSQL – metadata & job tracking

OpenRouter – LLM + embeddings

Docker Compose – local orchestration

🔌 Core API Endpoints
Ingest
POST /ingest


Triggers async document ingestion, chunking, embedding, and storage.

Retrieve & Generate
POST /retrieve


Performs semantic retrieval and returns a context-grounded LLM response.

Health
GET /health


Swagger UI available at:

/docs

🗄️ Persistence Model

Chroma (Vector DB)
Stores embeddings for semantic similarity search

PostgreSQL (Relational DB)
Stores ingestion jobs, processing state, and metadata

This avoids the common anti-pattern of storing system state in vector databases.

✅ RAG Capability Coverage

This repository fully implements:

Document ingestion

Text chunking

Embedding generation

Vector storage (Chroma)

Metadata layer (Postgres)

Semantic retrieval

Context-grounded generation

👉 Complete RAG loop implemented and verified

📌 Project Status

🔒 Frozen at Step 4 (RAG)

Evaluation, observability, and monitoring (Step 5) are intentionally excluded to keep this repository a clean RAG baseline.

⚙️ Run Locally
docker compose up --build


Environment variable required:

OPENAI_API_KEY=sk-or-xxxxxxxxxxxxxxxx


(OpenRouter key)

🎯 Why This Project Exists

This is a portfolio and learning milestone project built to demonstrate applied AI engineering skills, system design clarity, and real-world backend patterns — not a toy demo or UI app.
