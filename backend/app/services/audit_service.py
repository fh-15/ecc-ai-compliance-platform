from sqlalchemy.orm import Session
from datetime import datetime

from app.domain.audit_session import AuditAnswer
from app.domain.scoring import AuditScoringEngine
from app.domain.ecc_controls import ECC_CONTROLS

from app.repositories.audit_repository import AuditRepository


class AuditService:
    """
    Business logic layer for ECC audits.
    Uses Repository Layer for persistence.
    """

    def __init__(self):
        self.audit_repo = AuditRepository()
        self.scoring_engine = AuditScoringEngine()

    def start_audit(self, db: Session, user_id: int):
        """
        Starts a new audit session for a user.
        """
        return self.audit_repo.create_audit_session(db, user_id)

    def submit_answer(
        self,
        db: Session,
        session_id: int,
        control_code: str,
        question: str,
        answer: str,
        notes: str
    ):
        """
        Saves a single audit answer.
        """
        self.audit_repo.save_answer(
            db=db,
            session_id=session_id,
            control_code=control_code,
            question=question,
            answer=answer,
            notes=notes
        )

    def finalize_audit(self, db: Session, session_id: int):
        """
        Completes the audit and calculates the final score.
        """
        self.audit_repo.complete_audit(db, session_id)

        # Build a virtual AuditSession for scoring
        answers = []  # scoring will evolve later with DB queries

        score = self.scoring_engine.calculate_score_from_db(
            db=db,
            session_id=session_id,
            controls=ECC_CONTROLS
        )

        return score
