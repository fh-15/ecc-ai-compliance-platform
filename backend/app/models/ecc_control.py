from sqlalchemy import Column, Integer, String, Text
from app.db.base import Base


class ECCControl(Base):
    __tablename__ = "ecc_controls"

    id = Column(Integer, primary_key=True, index=True)
    domain = Column(String, nullable=False)
    control_code = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
