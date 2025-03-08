from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, func
from app.database.config import Base

class Prediction(Base):
    __tablename__ = 'prediction'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    model_id = Column(Integer, ForeignKey('model.id'), nullable=False)
    source_code_id = Column(Integer, ForeignKey('source_code.id'), nullable=False)
    is_feedback_submitted = Column(Boolean, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    modified_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    def __repr__(self):
        return f"<Prediction(id={self.id} model={self.model_id} source_code={self.source_code_id}>"