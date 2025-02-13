from sqlalchemy.orm import Session
from app.database.models.config import Config
from app.database.repositories.base import BaseRepository


class ConfigRepository(BaseRepository):
    def __init__(self, db: Session, model = Config):
        super().__init__(db, model)

    def get_by_name(self, name: str):
        return self.db.query(self.model).filter(self.model.name == name).first()