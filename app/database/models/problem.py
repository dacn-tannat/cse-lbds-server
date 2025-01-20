from sqlalchemy import Column, Integer, Text, ARRAY, JSON
from app.database.config import Base

class Problem(Base):
    __tablename__ = 'problem'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    category = Column(ARRAY(Text), nullable=True)
    level = Column(Text, nullable=True)
    image = Column(Text, nullable=True)
    constrain = Column(ARRAY(Text), nullable=True)
    testcase = Column(ARRAY(JSON), nullable=True)

    def __repr__(self):
        return f"<Problem(id={self.id}, name={self.name}>"