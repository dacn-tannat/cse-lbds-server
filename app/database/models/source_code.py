from sqlalchemy import Column, DateTime, Integer, Text, JSON, ARRAY, func
from app.database.config import Base

class SourceCode(Base):
    __tablename__ = "source_code"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    problem_id = Column(Integer, nullable=False)
    source_code = Column(Text, nullable=False)
    score = Column(Integer, nullable=True)
    verdict = Column(ARRAY(JSON), nullable=True)
    status = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    modified_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    def __repr__(self):
        return (
            f"<SourceCode(id={self.id}, problem_id={self.problem_id}, status={self.status}, user_id={self.user_id})>"
        )
