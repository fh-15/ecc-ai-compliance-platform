from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_user
from app.ai.engine import build_ai_engine

router = APIRouter(prefix="/ai", tags=["ai"])


@router.post("/assessment")
def generate_assessment(control_text: str):
    engine = build_ai_engine(mode="assessment")
    result = engine.run(control_text)
    return {"questions": result}


@router.post("/guidance")
def generate_guidance(control_text: str):
    engine = build_ai_engine(mode="guidance")
    result = engine.run(control_text)
    return {"guidance": result}
