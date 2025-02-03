from app.database.repositories.base import BaseRepository
from app.database.models.problem import Problem
from sqlalchemy.orm import Session

class ProblemRepository(BaseRepository):
    def __init__(self, db: Session, model = Problem):
        super().__init__(db, model)