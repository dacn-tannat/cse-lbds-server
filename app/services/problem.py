from typing import List
from app.database.models.problem import Problem
from app.database.repositories.problem import ProblemRepository
from fastapi import HTTPException

from app.database.schemas.problem import ProblemResponseSchema, TestCaseSchema

class ProblemService:
    def __init__(self, db):
        self.__problem_repository = ProblemRepository(db)

    def get_by_id(self, id):
        problem = self.__problem_repository.get_by_id(id)
        if problem is None:
            raise HTTPException(status_code=404, detail='Problem not found')
        return problem
    
    def get_problem(self, id) -> ProblemResponseSchema:
        problem: Problem = self.__problem_repository.get_by_id(id)
        if problem is None:
            raise HTTPException(status_code=404, detail='Problem not found')
        examples: List[TestCaseSchema] = []
        for testcase in problem.testcase:
            if testcase['is_example']:
                examples.append(TestCaseSchema(
                    testcode=testcase.get('testcode', None),
                    input=testcase.get('input', None),
                    output=testcase['output']
                ))
        return ProblemResponseSchema(
            id=problem.id,
            name=problem.name,
            description=problem.description,
            constrain=problem.constrain,
            examples=examples,
            category=problem.category,
            lab_id=problem.lab_id,
            is_active=problem.is_active
        )
    
    def get_all(self):
        return self.__problem_repository.get_all()
    
    def get_active_problems(self):
        return self.__problem_repository.get_active_problems()
