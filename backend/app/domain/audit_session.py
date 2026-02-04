from dataclasses import dataclass, field
from typing import Dict, List
from datetime import datetime
from app.domain.ecc_controls import ECCControl


@dataclass
class AuditAnswer:
    control_id: int
    question: str
    answer: str
    notes: str
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class AuditSession:
    session_id: int
    user_id: int
    started_at: datetime
    controls: List[ECCControl]
    answers: Dict[int, List[AuditAnswer]] = field(default_factory=dict)
    completed: bool = False

    def add_answer(self, answer: AuditAnswer):
        if answer.control_id not in self.answers:
            self.answers[answer.control_id] = []
        self.answers[answer.control_id].append(answer)

    def get_control_answers(self, control_id: int) -> List[AuditAnswer]:
        return self.answers.get(control_id, [])

