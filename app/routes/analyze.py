# app/routes/analyze.py
from fastapi import APIRouter
from app.schemas.analyze import AnalyzeRequest, AnalyzeResponse
from app.services.ai_service import analyze_text  # <-- direct function call

router = APIRouter()


@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze(payload: AnalyzeRequest):
    result = await analyze_text(payload.text)
    return {"status": "success", "result": result}
