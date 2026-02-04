from fastapi import APIRouter, Depends, HTTPException, status
from app.ai.engine import ECCAIEngine
from app.core.dependencies import get_current_user
from app.models.user import User
from app.schemas.ai import (
    AIAssessmentRequest,
    AIGuidanceRequest,
    AIResponse
)

router = APIRouter(prefix="/ai", tags=["AI"])

ai_engine = ECCAIEngine()


# ==================================================
# 1️⃣ Generate Assessment Questions
# ==================================================
@router.post(
    "/assessment",
    response_model=AIResponse,
    status_code=status.HTTP_200_OK
)
def generate_assessment(
    data: AIAssessmentRequest,
    current_user: User = Depends(get_current_user)
):
    try:
        result = ai_engine.run(
            query=data.control_context,
            mode="assessment"
        )
        return {"result": result}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


# ==================================================
# 2️⃣ Generate Guidance
# ==================================================
@router.post(
    "/guidance",
    response_model=AIResponse,
    status_code=status.HTTP_200_OK
)
def generate_guidance(
    data: AIGuidanceRequest,
    current_user: User = Depends(get_current_user)
):
    try:
        result = ai_engine.run(
            query=data.control_context,
            mode="guidance"
        )
        return {"result": result}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
