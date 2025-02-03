from sqlalchemy import ARRAY, JSON, Column, ForeignKey, Integer
from app.database.config import Base

class Prediction(Base):
    __tablename__ = 'prediction'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    model_id = Column(Integer, ForeignKey('model.id'), nullable=False)
    source_code_id = Column(Integer, ForeignKey('source_code.id'), nullable=False)
    buggy_position = Column(ARRAY(JSON), nullable=False)

    def __repr__(self):
        return f"<Prediction(id={self.id} model={self.model_id} source_code={self.source_code_id}>"