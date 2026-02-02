from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AuditSessionCreate(BaseModel):
    control_id: int


class AuditSessionResponse(BaseModel):
    id: int
    status: str
    started_at: datetime
    completed_at: Optional[datetime]

    class Config:
        from_attributes = True
