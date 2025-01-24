from sqlalchemy import Column, Integer, Text
from app.database.config import Base

class User(Base):
    __tablename__ = "user" 

    id = Column(Integer, primary_key=True, autoincrement=False) 
    email = Column(Text, nullable=False) 
    name = Column(Text, nullable=False) 
    model_type = Column(Text, nullable=False)

    def __repr__(self):
        return f"<User(id={self.id} name='{self.name}'>"
