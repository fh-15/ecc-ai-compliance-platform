from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class AuditAnswer(Base):
    __tablename__ = "audit_answers"

    id = Column(Integer, primary_key=True, index=True)

    audit_session_id = Column(
        Integer,
        ForeignKey("audit_sessions.id", ondelete="CASCADE"),
        nullable=False
    )

    question = Column(Text, nullable=False)
    answer = Column(String, nullable=False)
    notes = Column(Text, nullable=True)

    audit_session = relationship(
        "AuditSession",
        back_populates="answers"
    )
