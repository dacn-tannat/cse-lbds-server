from sqlalchemy import Column, DateTime, Integer, Text, func
from app.database.config import Base

class User(Base):
    __tablename__ = "user" 

    id = Column(Text, primary_key=True, autoincrement=False) 
    email = Column(Text, nullable=False) 
    name = Column(Text, nullable=False) 
    picture = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    modified_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    def __repr__(self):
        return f"<User(id={self.id} name='{self.name}'>"
