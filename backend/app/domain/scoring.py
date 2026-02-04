from app.domain.audit_session import AuditSession
from app.domain.ecc_controls import ECC_CONTROLS


class AuditScoringEngine:
    def calculate_score(self, session: AuditSession) -> dict:
        total_weight = sum(control.weight for control in ECC_CONTROLS)
        achieved_score = 0
        gaps = []

        for control in ECC_CONTROLS:
            answers = session.get_control_answers(control.id)

            if not answers:
                gaps.append({
                    "control": control.code,
                    "name": control.name,
                    "reason": "No answers provided",
                    "required_evidence": control.required_evidence
                })
                continue

            positive_answers = [
                a for a in answers if a.answer.lower() in ["yes", "implemented", "available"]
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

        compliance_percentage = round((achieved_score / total_weight) * 100, 2)

        return {
            "score_percentage": compliance_percentage,
            "gaps": gaps
        }

