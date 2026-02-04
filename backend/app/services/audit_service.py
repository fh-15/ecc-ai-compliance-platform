from datetime import datetime
from app.domain.audit_session import AuditSession, AuditAnswer
from app.domain.ecc_controls import ECC_CONTROLS
from app.domain.scoring import AuditScoringEngine


class AuditService:
    def __init__(self):
        self.sessions = {}
        self.scoring_engine = AuditScoringEngine()

    def start_audit(self, user_id: int) -> AuditSession:
        session_id = len(self.sessions) + 1
        session = AuditSession(
            session_id=session_id,
            user_id=user_id,
            started_at=datetime.utcnow(),
            controls=ECC_CONTROLS
        )
        self.sessions[session_id] = session
        return session

    def submit_answer(
        self,
        session_id: int,
        control_id: int,
        question: str,
        answer: str,
        notes: str
    ):
        session = self.sessions.get(session_id)
        if not session:
            raise ValueError("Audit session not found")

        audit_answer = AuditAnswer(
            control_id=control_id,
            question=question,
            answer=answer,
            notes=notes
        )
        session.add_answer(audit_answer)

    def finalize_audit(self, session_id: int):
        session = self.sessions.get(session_id)
        if not session:
            raise ValueError("Audit session not found")

        session.completed = True
        return self.scoring_engine.calculate_score(session)

