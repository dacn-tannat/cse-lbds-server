from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.config import get_db
from app.services.source_code import SourceCodeService
from app.database.schemas.source_code import SourceCodeRequestSchema
from app.services.problem import ProblemService

sourceCodeRouter = APIRouter()

@sourceCodeRouter.get('/')
def get_source_codes(db: Session = Depends(get_db)):
    try:
        return SourceCodeService(db).get_all()
    except Exception as e:
        print(e)
        raise e

@sourceCodeRouter.post('/submit')
async def create_source_code(source_code_request: SourceCodeRequestSchema, db: Session = Depends(get_db)):
    try:
        problem = ProblemService(db).get_by_id(source_code_request.problem_id)
        return await SourceCodeService(db).submit(source_code_request.source_code, problem.testcase)
    except Exception as e:
        print(e)
        raise e