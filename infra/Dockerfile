FROM python:3.11-slim

WORKDIR /app

COPY ../requirements.txt .

RUN  pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY ../app ./app

# Set working directory to app folder where FastAPI main.py is located
WORKDIR /app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
