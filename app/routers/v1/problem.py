from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.auth.google_auth import get_current_user
from app.database.config import get_db
from app.services.problem import ProblemService

problemRouter = APIRouter()

@problemRouter.get('/')
def get_problems(db: Session = Depends(get_db)):
    """API lấy thông tin tất cả problem trong db."""
    try:
        return ProblemService(db).get_all()
    except Exception as e:
        print(e)
        raise e

@problemRouter.get('/{id}')
def get_problem_by_id(id: int, db: Session = Depends(get_db)):
    """API lấy thông tin của một problem bằng id."""
    try:
        return ProblemService(db).get_by_id(id)
    except Exception as e:
        print(e)
        raise e
    
@problemRouter.get('/protected')
def get_problems(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    """API lấy thông tin tất cả problem trong db."""
    print(current_user)
    try:
        return ProblemService(db).get_all()
    except Exception as e:
        print(e)
        raise e