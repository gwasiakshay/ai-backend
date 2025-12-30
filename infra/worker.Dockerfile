FROM python:3.11-slim

WORKDIR /worker

COPY ../requirements.txt .
RUN  pip install --no-cache-dir -r requirements.txt

COPY ../app ./app
COPY ../main.py .
COPY ../db.py .
COPY ../models.py .

CMD ["python", "-c", "import asyncio; from app.services.ai_service import process_jobs_loop; asyncio.run(process_jobs_loop())"]
