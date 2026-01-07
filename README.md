# 🧠 AI Backend — Async FastAPI + Background Worker + Docker + Postgres

Production-grade backend powering AI text-processing jobs.  
Built with **FastAPI**, **async SQLAlchemy**, **Docker multi-container**, and **OpenRouter Chat Completions**.

---

## 🚀 Features
- Async FastAPI API (analyze + job queue)
- Background worker for long-running AI tasks
- PostgreSQL persistence (status + result)
- Docker-based infra (backend + worker + db)
- Structured logging
- OpenRouter AI model support (`gpt-4o-mini` etc.)

---

## 🧱 Architecture
📦 ai-backend
├── app/
│ ├── main.py ← FastAPI entrypoint
│ ├── routes/ ← API routes
│ ├── services/ ← AI + DB logic
│ ├── core/ ← env / logging
│ ├── worker/ ← background job runner
│ └── schemas/ ← Pydantic models
├── infra/
│ ├── docker-compose.yml
│ └── Dockerfile
├── .env.example ← copy to .env and fill
└── requirements.txt


---

## 🧪 Local Run — Without Docker
```bash
cd ai-backend
uvicorn app.main:app --reload

**## Run With Docker (recommended)**

cd ai-backend/infra
docker compose up --build

