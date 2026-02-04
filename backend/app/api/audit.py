from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.services.db_service import get_db
from app.services.audit_service import AuditService
from app.core.dependencies import get_current_user
from app.models.user import User
from app.schemas.audit import (
    StartAuditResponse,
    SubmitAnswerRequest,
    AuditResultResponse
)

router = APIRouter(prefix="/audit", tags=["audit"])

audit_service = AuditService()


# ==================================================
# 1️⃣ Start Audit
# ==================================================
@router.post("/start", response_model=StartAuditResponse)
def start_audit(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    session = audit_service.start_audit(db, current_user.id)
    return {"session_id": session.id}


# ==================================================
# 2️⃣ Submit Answer
# ==================================================
@router.post("/answer", status_code=status.HTTP_200_OK)
def submit_answer(
    data: SubmitAnswerRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    audit_service.submit_answer(
        db=db,
        session_id=data.session_id,
        control_code=data.control_code,
        question=data.question,
        answer=data.answer,
        notes=data.notes
    )
    return {"status": "answer saved"}


# ==================================================
# 3️⃣ Finalize Audit + Score
# ==================================================
@router.post("/finalize", response_model=AuditResultResponse)
def finalize_audit(
    session_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = audit_service.finalize_audit(db, session_id)
    return result
