from sqlalchemy.orm import Session
from app.db.models import AuditAnswerModel


class AuditScoringEngine:
    """
    Calculates ECC compliance score and identifies gaps
    using persisted audit data from the database.
    """

    def calculate_score_from_db(
        self,
        db: Session,
        session_id: int,
        controls: list
    ) -> dict:
        """
        Calculate compliance percentage and gaps for an audit session.

        Args:
            db (Session): SQLAlchemy database session
            session_id (int): Audit session ID
            controls (list): List of ECC controls

        Returns:
            dict: {
                "score_percentage": float,
                "gaps": list
            }
        """

        total_weight = sum(control.weight for control in controls)
        achieved_score = 0
        gaps = []

        for control in controls:
            # Fetch all answers for this control from DB
            answers = db.query(AuditAnswerModel).filter(
                AuditAnswerModel.session_id == session_id,
                AuditAnswerModel.control_code == control.code
            ).all()

            # No answers provided → gap
            if not answers:
                gaps.append({
                    "control": control.code,
                    "name": control.name,
                    "reason": "No answers provided",
                    "required_evidence": control.required_evidence
                })
                continue

            # Check for positive implementation answers
            positive_answers = [
                answer for answer in answers
                if answer.answer.lower() in ["yes", "implemented", "available"]
            ]

            if positive_answers:
                achieved_score += control.weight
            else:
                gaps.append({
                    "control": control.code,
                    "name": control.name,
                    "reason": "Control not implemented",
                    "required_evidence": control.required_evidence
                })

        # Calculate final compliance percentage safely
        compliance_percentage = (
            round((achieved_score / total_weight) * 100, 2)
            if total_weight > 0
            else 0.0
        )

        return {
            "score_percentage": compliance_percentage,
            "gaps": gaps
        }
