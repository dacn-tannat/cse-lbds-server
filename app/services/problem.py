from app.database.repositories.problem import ProblemRepository
from fastapi import HTTPException

class ProblemService:
    def __init__(self, db):
        self.__problem_repository = ProblemRepository(db)

    def get_by_id(self, id):
        problem = self.__problem_repository.get_by_id(id)
        if problem is None:
            raise HTTPException(status_code=404, detail='Problem not found')
        return problem
    
    def get_all(self):
        return self.__problem_repository.get_all()
