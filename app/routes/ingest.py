from fastapi import APIRouter
from pydantic import BaseModel
from app.rag.ingest import ingest_text

router = APIRouter()


class IngestRequest(BaseModel):
    text: str


@router.post("/ingest")
def ingest_endpoint(req: IngestRequest):
    count = ingest_text(req.text)
    return {"chunks_added": count}
