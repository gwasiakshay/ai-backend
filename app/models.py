# app/models.py
from sqlalchemy import Column, Integer, String, Text, JSON
from sqlalchemy.orm import declarative_base

from app.db import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, default="pending")
    text = Column(Text, nullable=False)
    result = Column(JSON, nullable=True)
    error = Column(String, nullable=True)
