# app/schemas/analyze.py
from pydantic import BaseModel
from typing import Any


class AnalyzeRequest(BaseModel):
    text: str


class AnalyzeResponse(BaseModel):
    status: str
    result: Any  # <-- FIX (was str)
