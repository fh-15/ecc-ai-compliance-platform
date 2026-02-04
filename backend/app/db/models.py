from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from datetime import datetime
from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class AuditSessionModel(Base):
    __tablename__ = "audit_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    started_at = Column(DateTime, default=datetime.utcnow)
    completed = Column(Boolean, default=False)


class AuditAnswerModel(Base):
    __tablename__ = "audit_answers"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("audit_sessions.id"))
    control_code = Column(String, nullable=False)
    question = Column(Text, nullable=False)
    answer = Column(String, nullable=False)
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
