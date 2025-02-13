from typing import List
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database.config import get_db
from app.database.schemas.problem import ProblemOverviewResponseSchema, ProblemResponseSchema
from app.services.problem import ProblemService
from app.auth.google_auth import get_current_user

problemRouter = APIRouter()

@problemRouter.get('/active', response_model=List[ProblemOverviewResponseSchema])
def get_problems(db: Session = Depends(get_db)):
    """API lấy thông tin tất cả problem active trong db."""
    try:
        return ProblemService(db).get_active_problems()
    except Exception as e:
        print(e)
        raise e

@problemRouter.get('/{id}', response_model=ProblemResponseSchema)
def get_problem_by_id(id: int, db: Session = Depends(get_db)):
    """API lấy thông tin của một problem bằng id."""
    try:
        return ProblemService(db).get_problem(id)
    except Exception as e:
        print(e)
        raise e
    
@problemRouter.get('/protected/{id}')
def get_problem_by_id(id: int, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    """API lấy thông tin của một problem bằng id."""
    try:
        return ProblemService(db).get_problem(id)
    except Exception as e:
        print(e)
        raise e