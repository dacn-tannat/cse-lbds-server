from typing import List
from app.database.repositories.base import BaseRepository
from app.database.models.problem import Problem
from sqlalchemy.orm import Session

from app.database.schemas.problem import ProblemOverviewResponseSchema

class ProblemRepository(BaseRepository):
    def __init__(self, db: Session, model = Problem):
        super().__init__(db, model)

    def get_active_problems(self) -> List[ProblemOverviewResponseSchema]:
        return self.db.query(Problem.id, Problem.name, Problem.lab_id, Problem.category, Problem.is_active).filter(Problem.is_active == True).all()