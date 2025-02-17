from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.database.models.config import Config
from app.database.repositories.base import BaseRepository


class ConfigRepository(BaseRepository):
    def __init__(self, db: Session, model = Config):
        super().__init__(db, model)

    def get_by_name(self, name: str):
        model = self.db.query(self.model).filter(self.model.name == name).first()
        if model is None:
            return HTTPException(status_code=404, detail='Configuration in model type get errors.')
        return model
