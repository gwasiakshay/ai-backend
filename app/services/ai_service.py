# app/services/ai_service.py
import json
import os
import asyncio
import logging
from dotenv import load_dotenv
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError, ProgrammingError
from openai import AsyncOpenAI

from app.models import Job
from app.db import AsyncSessionLocal

# ------------ Logging ------------
logger = logging.getLogger("worker")

# ------------ Load API Key ------------
load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

client = AsyncOpenAI(
    api_key=OPENAI_KEY,
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "http://localhost",
        "X-Title": "ai-backend-dev",
    },
)


# ============================================================
# 🔹 AI TEXT ANALYZER
# ============================================================
async def analyze_text(text: str) -> dict:
    try:
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    Return ONLY valid JSON. 
                    Analyze this text: "{text}"

                    {{
                        "uppercase": STRING,
                        "length": NUMBER
                    }}
                    """,
                }
            ],
        )
        raw = response.choices[0].message.content
        return json.loads(raw)

    except Exception as e:
        logger.error(f"LLM Request Failed :: {e}")
        return {"error": str(e)}


# ============================================================
# 🔹 Create Job
# ============================================================
async def enqueue_job(text: str, db: AsyncSession) -> str:
    job = Job(text=text, status="pending", result=None)
    db.add(job)
    await db.commit()
    await db.refresh(job)
    logger.info(f"🆕 Job {job.id} created")
    return job.id


# ============================================================
# 🔹 Fetch Job
# ============================================================
async def get_job(job_id: str, db: AsyncSession):
    try:
        job_id = int(job_id)
    except ValueError:
        logger.warning(f"Invalid job_id: {job_id}")
        return None

    result = await db.execute(select(Job).where(Job.id == job_id))
    job = result.scalar_one_or_none()
    return job


# ============================================================
# 🔹 Worker Loop (Async Processor)
# ============================================================
async def process_jobs_loop():
    logger.info("🧵 Worker STARTED")
    quiet = 0

    while True:
        try:
            async with AsyncSessionLocal() as session:
                result = await session.execute(
                    select(Job).where(Job.status == "pending").limit(1)
                )
                job = result.scalars().first()

                if not job:
                    logger.info("⏳ Worker idle...")
                    await asyncio.sleep(5)
                    continue

                # quiet = 0
                logger.info(f"⚙️ Processing Job {job.id} → {job.text}")

                output = await analyze_text(job.text)

                job.status = "completed"
                job.result = json.dumps(output)

                await session.commit()
                logger.info(f"🎉 Job {job.id} done")

        except ProgrammingError:
            logger.warning("⏳ Tables not ready yet — waiting...")
            await asyncio.sleep(5)

        except Exception as e:
            logger.exception("🔥 Worker fatal error")
            await asyncio.sleep(5)
