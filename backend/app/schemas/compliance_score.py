from pydantic import BaseModel
from datetime import datetime


class ComplianceScoreResponse(BaseModel):
    score_percentage: float
    gaps_count: int
    calculated_at: datetime

    class Config:
        from_attributes = True
