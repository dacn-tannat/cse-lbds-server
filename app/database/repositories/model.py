from app.database.models.model import Model
from app.database.repositories.base import BaseRepository
from sqlalchemy.orm import Session

class ModelRepository(BaseRepository):
    def __init__(self, db: Session, model = Model):
        super().__init__(db, model)

    def get_by_type_and_problem(self, type: int, problem_id: int):
        return self.db.query(self.model).filter(self.model.model_type == type, self.model.problem_id == problem_id).first()