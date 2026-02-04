from pydantic import BaseModel


class AIAssessmentRequest(BaseModel):
    control_context: str


class AIGuidanceRequest(BaseModel):
    control_context: str


class AIResponse(BaseModel):
    result: str
