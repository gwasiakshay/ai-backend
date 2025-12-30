from pydantic import BaseModel
from typing import Optional, Dict, Any


class JobCreateRequest(BaseModel):
    text: str


class JobResponse(BaseModel):
    job_id: int
    status: str
    result: Optional[Dict[str, Any]] = None
