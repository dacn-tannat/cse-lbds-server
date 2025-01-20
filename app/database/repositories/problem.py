from app.database.repositories.base import BaseRepository
from app.database.models.problem import Problem
from sqlalchemy.orm import Session

class ProblemRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db)

    def get_all(self):
        return self.db.query(Problem).all()

    def get_by_id(self, id):
        return self.db.query(Problem).filter(Problem.id == id).first()