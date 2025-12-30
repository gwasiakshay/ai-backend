# app/routes/jobs.py
import json
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.jobs import JobCreateRequest, JobResponse
from app.services.ai_service import enqueue_job, get_job
from app.db import get_db

router = APIRouter()


# -----------------------------
# CREATE JOB
# -----------------------------
@router.post("/jobs", response_model=JobResponse)
async def create_job_endpoint(
    payload: JobCreateRequest, db: AsyncSession = Depends(get_db)
):
    job_id = await enqueue_job(payload.text, db)
    return {"job_id": job_id, "status": "pending", "result": None}


# -----------------------------
# GET JOB STATUS
# -----------------------------
@router.get("/jobs/{job_id}", response_model=JobResponse)
async def get_job_endpoint(job_id: int, db: AsyncSession = Depends(get_db)):
    job = await get_job(job_id, db)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    # NEW FIX:
    result = job.result
    if isinstance(result, str):
        try:
            result = json.loads(result)
        except:  # noqa: E722
            result = None

    return {"job_id": job.id, "status": job.status, "result": result}
