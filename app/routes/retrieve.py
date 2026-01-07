from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.retrieve import retrieve_chunks
from app.rag.generate import generate_answer

router = APIRouter()


class RetrieveRequest(BaseModel):
    query: str


@router.post("/retrieve")
async def retrieve(req: RetrieveRequest):
    chunks = retrieve_chunks(req.query)

    answer = await generate_answer(
        question=req.query,
        context_chunks=chunks,
    )

    return {
        "query": req.query,
        "answer": answer,
        "context": chunks,
    }
