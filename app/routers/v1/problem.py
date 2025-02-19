from typing import List
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database.config import get_db
from app.database.schemas.generic_response import GenericResponse
from app.database.schemas.problem import ProblemOverviewResponseSchema, ProblemResponseSchema
from app.services.auth import AuthService
from app.services.problem import ProblemService

problemRouter = APIRouter()
auth_service = AuthService()

@problemRouter.get('/active', response_model=GenericResponse[List[ProblemOverviewResponseSchema]])
def get_problems(user: dict = Depends(auth_service.get_current_user), db: Session = Depends(get_db)):
    """API lấy thông tin tất cả problem active trong db."""
    try:
        return GenericResponse(data=ProblemService(db).get_active_problems())
    except Exception as e:
        raise e
    
@problemRouter.get('/{id}', response_model=GenericResponse[ProblemResponseSchema])
def get_problem_by_id(id: int, user: dict = Depends(auth_service.get_current_user), db: Session = Depends(get_db)):
    """API lấy thông tin của một problem bằng id."""
    try:
        return GenericResponse(data=ProblemService(db).get_problem(id))
    except Exception as e:
        raise e