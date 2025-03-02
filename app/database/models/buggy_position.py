from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, PrimaryKeyConstraint, Text, func
from app.database.config import Base


class BuggyPosition(Base):
    __tablename__ = 'buggy_position'

    id = Column(Integer, nullable=False)
    prediction_id = Column(Integer, ForeignKey('prediction.id'), nullable=False)
    position = Column(Integer, nullable=False)
    start_index = Column(Integer, nullable=False)
    original_token = Column(Text, nullable=False)
    line_number = Column(Integer, nullable=False)
    predicted_token = Column(Text, nullable=False)
    is_token_error = Column(Boolean, default=False)
    is_suggestion_useful = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    modified_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', 'prediction_id'),  # Định nghĩa Composite Key
    )

    def __repr__(self):
        return f"<BuggyPosition(id={self.id} source_code={self.source_code_id} position={self.position} start_index={self.start_index} original_token='{self.original_token}'>"