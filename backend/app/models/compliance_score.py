from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from datetime import datetime
from app.db.base import Base


class ComplianceScore(Base):
    __tablename__ = "compliance_scores"

    id = Column(Integer, primary_key=True, index=True)

    audit_session_id = Column(
        Integer,
        ForeignKey("audit_sessions.id", ondelete="CASCADE"),
        nullable=False,
        unique=True
    )

    score_percentage = Column(Float, nullable=False)
    gaps_count = Column(Integer, nullable=False)

    calculated_at = Column(DateTime, default=datetime.utcnow)
