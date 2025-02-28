from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.database.models.buggy_position import BuggyPosition
from app.database.repositories.base import BaseRepository


class BuggyPositionRepository(BaseRepository):
    def __init__(self, db: Session, model = BuggyPosition):
        super().__init__(db, model)

    def get_by_prediction_id(self, prediction_id):
        prediction = self.db.query(BuggyPosition).filter(BuggyPosition.prediction_id == prediction_id).all()
        if prediction is None:
            raise HTTPException(status_code=404, detail='Prediction not found')
        return prediction
    
    def update(self, id, prediction_id, data):
        buggy_position = self.db.query(BuggyPosition).filter(BuggyPosition.id == id, BuggyPosition.prediction_id == prediction_id).first()
        if buggy_position is None:
            raise HTTPException(status_code=404, detail='Buggy position not found')
        for key, value in data.items():
            setattr(buggy_position, key, value)
        self.db.commit()
        return buggy_position