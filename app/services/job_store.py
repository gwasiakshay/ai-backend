import uuid
from typing import Dict
from app.schemas.jobs import JobStatus


jobs: Dict[str, dict] = {}


def create_job() -> str:
    job_id = str(uuid.uuid4())
    jobs[job_id] = {
        "status": JobStatus.pending,
        "result": None,
    }
    return job_id


def update_job(job_id: str, status: JobStatus, result=None):
    jobs[job_id]["status"] = status
    jobs[job_id]["result"] = result


def get_job(job_id: str):
    return jobs.get(job_id)
