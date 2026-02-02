from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(String, default="user")
    created_at = Column(DateTime, default=datetime.utcnow)

    audit_sessions = relationship(
        "AuditSession",
        back_populates="user",
        cascade="all, delete-orphan"
    )
