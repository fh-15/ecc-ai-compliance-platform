from sqlalchemy.orm import Session
from app.db.models import AuditSessionModel, AuditAnswerModel


class AuditRepository:

    def create_audit_session(self, db: Session, user_id: int) -> AuditSessionModel:
        session = AuditSessionModel(
            user_id=user_id
        )
        db.add(session)
        db.commit()
        db.refresh(session)
        return session

    def save_answer(
        self,
        db: Session,
        session_id: int,
        control_code: str,
        question: str,
        answer: str,
        notes: str
    ):
        audit_answer = AuditAnswerModel(
            session_id=session_id,
            control_code=control_code,
            question=question,
            answer=answer,
            notes=notes
        )
        db.add(audit_answer)
        db.commit()

    def complete_audit(self, db: Session, session_id: int):
        session = db.query(AuditSessionModel).filter(
            AuditSessionModel.id == session_id
        ).first()

        if session:
            session.completed = True
            db.commit()
