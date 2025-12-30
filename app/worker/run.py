import asyncio
from dotenv import load_dotenv
from app.services.ai_service import process_jobs_loop

load_dotenv()

if __name__ == "__main__":
    asyncio.run(process_jobs_loop())
