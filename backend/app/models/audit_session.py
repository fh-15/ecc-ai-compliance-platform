from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base


class AuditSession(Base):
    __tablename__ = "audit_sessions"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    control_id = Column(Integer, ForeignKey("ecc_controls.id"), nullable=False)

    status = Column(String, default="in_progress")

    started_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="audit_sessions")
    control = relationship("ECCControl", back_populates="audit_sessions")

    answers = relationship(
        "AuditAnswer",
        back_populates="audit_session",
        cascade="all, delete-orphan"
    )

    score = relationship(
        "ComplianceScore",
        back_populates="audit_session",
        uselist=False,
        cascade="all, delete-orphan"
    )
