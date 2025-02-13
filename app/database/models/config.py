from sqlalchemy import JSON, Column, DateTime, ForeignKey, Integer, Text, func
from app.database.config import Base

class Config(Base):
    __tablename__ = 'config'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(Text, nullable=False)
    value = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    modified_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)