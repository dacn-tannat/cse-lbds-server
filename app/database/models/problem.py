from sqlalchemy import Boolean, Column, DateTime, Integer, Text, ARRAY, JSON, func
from app.database.config import Base

class Problem(Base):
    __tablename__ = 'problem'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    constrain = Column(ARRAY(Text), nullable=True)
    testcase = Column(ARRAY(JSON), nullable=True)
    category = Column(Text, nullable=True)
    lab_id = Column(Integer, nullable=True)
    is_active = Column(Boolean, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    modified_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    def __repr__(self):
        return f"<Problem(id={self.id}, name={self.name}>"