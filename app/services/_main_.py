import asyncio
from app.services.ai_service import process_jobs_loop

if __name__ == "__main__":
    asyncio.run(process_jobs_loop())
