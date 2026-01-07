AI Backend – Retrieval-Augmented Generation (RAG)

This repository contains a production-style AI backend that implements a complete Retrieval-Augmented Generation (RAG) pipeline.

The project is built to demonstrate applied AI engineering principles, focusing on clean architecture, separation of concerns, and real-world backend patterns.

📌 Project Status

✅ Step 4 (RAG) – Complete and Frozen

This repository is intentionally frozen at Step 4 of the AI Engineer roadmap.
Evaluation, observability, and monitoring (Step 5) are not included by design.

🧠 What This Project Does

At a high level, this backend:

Ingests raw text documents

Splits them into chunks

Generates embeddings

Stores embeddings in a vector database

Stores metadata and job state in PostgreSQL

Retrieves relevant context using semantic search

Generates grounded answers using an LLM

In short:

Documents → Embeddings → Vector Search → Context → LLM Answer

🏗️ Architecture Overview
Core Components

FastAPI – REST API layer

Background Worker – Asynchronous ingestion and processing

Chroma – Vector database for semantic search

PostgreSQL – Metadata and job state storage

OpenRouter – LLM + embeddings provider

Docker Compose – Local orchestration

Design Principles

Thin API routes

Business logic isolated in services

Clear separation between:

semantic memory (vectors)

system state (relational DB)

Async-safe ingestion pipeline

Provider-agnostic LLM abstraction

📂 Project Structure (Simplified)
ai-backend/
├── app/
│   ├── routes/        # FastAPI endpoints
│   ├── rag/           # Retrieval + generation logic
│   ├── db/            # PostgreSQL models & session
│   ├── vectorstore/   # Chroma interface
│   └── config/        # Settings & environment loading
│
├── worker/
│   └── worker.py      # Background ingestion worker
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md

🔌 API Endpoints
Health
GET /health

Ingest Document
POST /ingest


Request

{
  "text": "Your document text here"
}


This triggers:

chunking

embedding generation

vector storage

metadata persistence

Processing is handled asynchronously by the worker.

Retrieve & Generate Answer
POST /retrieve


Request

{
  "query": "What is Retrieval-Augmented Generation?"
}


Response

Grounded answer generated from retrieved context

Retrieved context included for transparency

🗄️ Persistence Model
Vector Store (Chroma)

Stores chunk embeddings

Used for semantic similarity search

Relational Database (PostgreSQL)

Stores ingestion jobs

Tracks processing status

Maintains structured system metadata

This dual-store approach avoids overloading the vector DB with system state.

⚙️ Running Locally
Prerequisites

Docker

Docker Compose

Environment Variables

Create a .env file in the project root:

OPENAI_API_KEY=sk-or-xxxxxxxxxxxxxxxxxxxx


⚠️ Use an OpenRouter API key (sk-or-...), not a direct OpenAI key.

Start the system
docker compose up --build


Then open:

http://127.0.0.1:8000/docs

🧪 Verified Functionality

✅ Document ingestion

✅ Text chunking

✅ Embeddings generation

✅ Vector storage (Chroma)

✅ Metadata layer (Postgres)

✅ Semantic retrieval

✅ Context-grounded generation

🧭 Roadmap Alignment

This project completes Step 4 – Retrieval-Augmented Generation.

Step	Status
Document ingestion	✅
Text chunking	✅
Embeddings	✅
Vector store (Chroma)	✅
Metadata layer (Postgres)	✅
Retrieval	✅
Generation	✅
🔒 Freeze Notice

This repository is intentionally frozen at Step 4.

Future work such as:

evaluation

observability

tracing

guardrails

will be developed in a separate branch or repository.

🎯 Why This Project Exists

This project demonstrates the ability to:

Design AI systems end-to-end

Build production-style backends

Apply RAG correctly (not prompt stuffing)

Separate semantic memory from system state

Debug real LLM integration issues

It is intended as a learning milestone and portfolio project, not a full product.
