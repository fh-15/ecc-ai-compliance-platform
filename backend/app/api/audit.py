from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.core.dependencies import get_current_user
from app.models.audit_session import AuditSession
from app.models.ecc_control import ECCControl
from app.schemas.audit_session import AuditSessionCreate, AuditSessionResponse
from app.models.user import User

router = APIRouter(prefix="/audit", tags=["audit"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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
