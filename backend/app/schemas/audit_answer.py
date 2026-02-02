from pydantic import BaseModel


class AuditAnswerCreate(BaseModel):
    question: str
    answer: str
    notes: str | None = None


class AuditAnswerResponse(BaseModel):
    id: int
    question: str
    answer: str
    notes: str | None

    class Config:
        from_attributes = True
