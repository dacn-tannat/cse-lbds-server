from sqlalchemy import JSON, Column, DateTime, ForeignKey, Integer, Text, func
from app.database.config import Base

class Model(Base):
    __tablename__ = 'model'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    model_type = Column(Text, nullable=False)
    model_path = Column(Text, nullable=False)
    hyperparameter = Column(JSON, nullable=True)
    problem_id = Column(Integer, ForeignKey('problem.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    modified_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    def __repr__(self):
        return f"<Model(id={self.id} model_type='{self.model_type}'>"