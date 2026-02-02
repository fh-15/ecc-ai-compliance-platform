from app.models.audit_answer import AuditAnswer
from app.schemas.audit_answer import AuditAnswerCreate, AuditAnswerResponse


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
