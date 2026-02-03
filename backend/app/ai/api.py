from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/ai", tags=["ai"])


@router.post("/assessment")
def generate_questions(control_id: int):
    return {
        "message": "Assessment questions will be generated here"
    }


@router.post("/guidance")
def generate_guidance(control_id: int):
    return {
        "message": "Guidance will be generated here"
    }
