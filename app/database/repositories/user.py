from sqlalchemy.orm import Session
from app.database.models.user import User
from app.database.repositories.base import BaseRepository

class UserRepository(BaseRepository):
    def __init__(self, db: Session, model = User):
        super().__init__(db, model)