from app.database.models.prediction import Prediction
from app.database.repositories.base import BaseRepository
from sqlalchemy.orm import Session

class PredictionRepository(BaseRepository):
    def __init__(self, db: Session, model = Prediction):
        super().__init__(db, model)