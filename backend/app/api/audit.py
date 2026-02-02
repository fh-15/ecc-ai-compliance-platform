from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime

from app.db.session import SessionLocal
from app.core.dependencies import get_current_user
from app.models.user import User
from app.models.ecc_control import ECCControl
from app.models.audit_session import AuditSession
from app.models.audit_answer import AuditAnswer
from app.models.compliance_score import ComplianceScore

from app.schemas.audit_session import AuditSessionCreate, AuditSessionResponse
from app.schemas.audit_answer import AuditAnswerCreate, AuditAnswerResponse
from app.schemas.compliance_score import ComplianceScoreResponse

router = APIRouter(prefix="/audit", tags=["audit"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -----------------------------
# 1️⃣ Start Audit Session
# -----------------------------
@router.post(
    "/start",
    response_model=AuditSessionResponse,
    status_code=status.HTTP_201_CREATED
)
def start_audit(
    data: AuditSessionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    control = db.query(ECCControl).filter(
        ECCControl.id == data.control_id
    ).first()

    if not control:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="ECC control not found"
        )

    audit = AuditSession(
        user_id=current_user.id,
        control_id=control.id
    )
    db.add(audit)
    db.commit()
    db.refresh(audit)
    return audit


# -----------------------------
# 2️⃣ Submit Audit Answer
# -----------------------------
@router.post(
    "/answer/{audit_id}",
    response_model=AuditAnswerResponse,
    status_code=status.HTTP_201_CREATED
)
def submit_answer(
    audit_id: int,
    data: AuditAnswerCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    audit = db.query(AuditSession).filter(
        AuditSession.id == audit_id,
        AuditSession.user_id == current_user.id
    ).first()

    if not audit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Audit session not found"
        )

    answer = AuditAnswer(
        audit_session_id=audit.id,
        question=data.question,
        answer=data.answer,
        notes=data.notes
    )

    db.add(answer)
    db.commit()
    db.refresh(answer)
    return answer


# -----------------------------
# 3️⃣ Calculate Compliance Score
# -----------------------------
@router.post(
    "/score/{audit_id}",
    response_model=ComplianceScoreResponse,
    status_code=status.HTTP_200_OK
)
def calculate_score(
    audit_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    audit = db.query(AuditSession).filter(
        AuditSession.id == audit_id,
        AuditSession.user_id == current_user.id
    ).first()

    if not audit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Audit session not found"
        )

    # منع إعادة الحساب
    existing_score = db.query(ComplianceScore).filter(
        ComplianceScore.audit_session_id == audit.id
    ).first()

    if existing_score:
        return existing_score

    answers = audit.answers
    if not answers:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No answers submitted for this audit"
        )

    total = len(answers)
    compliant = sum(1 for a in answers if a.answer.lower() == "yes")
    gaps = total - compliant

    score_percentage = (compliant / total) * 100

    score = ComplianceScore(
        audit_session_id=audit.id,
        score_percentage=round(score_percentage, 2),
        gaps_count=gaps
    )

    audit.status = "completed"
    audit.completed_at = datetime.utcnow()

    db.add(score)
    db.commit()
    db.refresh(score)

    return score
