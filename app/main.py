# app/main.py
import os
import logging
import asyncio
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager

from app.routes.health import router as health_router
from app.routes.analyze import router as analyze_router
from app.routes.jobs import router as jobs_router

from app.db import engine, Base
from app.services.ai_service import process_jobs_loop

from dotenv import load_dotenv

from app.routes import ingest, retrieve

load_dotenv()

# -------- LOGGING (BASIC) --------
logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] %(levelname)s :: %(message)s"
)
logger = logging.getLogger("ai-backend")


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_dotenv()
    key = os.getenv("OPENAI_API_KEY")

    logger.info("🚀 Starting AI backend...")

    async with engine.begin() as conn:
        logger.info("🔧 Creating DB tables...")
        await conn.run_sync(Base.metadata.create_all)

    # ---- ENV Check Logging ----
    if key:
        logger.info("🔑 ENV Loaded: OPENAI_API_KEY FOUND")
    else:
        logger.error("❌ OPENAI_API_KEY NOT FOUND — check .env !")

    # ---- Start Background Worker ----
    asyncio.create_task(process_jobs_loop())

    yield
    logger.info("👋 Backend shutdown...")


# -------- FASTAPI APP --------
app = FastAPI(title="AI Backend", version="1.0", lifespan=lifespan)

app.include_router(health_router, tags=["health"])
app.include_router(analyze_router, tags=["analyze"])
app.include_router(jobs_router, tags=["jobs"])


# -------- GLOBAL EXCEPTION HANDLER --------
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "detail": str(exc)},
    )


app.include_router(ingest.router, tags=["ingest"])
app.include_router(retrieve.router, tags=["retrieve"])
