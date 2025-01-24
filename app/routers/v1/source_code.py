from fastapi import APIRouter, Depends
from datetime import datetime
import pytz
from sqlalchemy.orm import Session
from app.database.config import get_db
from app.database.models.source_code import SourceCode
from app.services.source_code import SourceCodeService
from app.database.schemas.source_code import SourceCodeRequestSchema, SourceCodeResponseSchema
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
        output = await SourceCodeService(db).submit(source_code_request.source_code, problem.testcase)
        source_code = SourceCode(
            problem_id=source_code_request.problem_id,
            source_code=source_code_request.source_code,
            status=output['status'],
            submit_time=datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')),
            score=output.get('score', None),
            verdict=output.get('verdict', None),
            user_id=0
        )
        SourceCodeService(db).create(source_code, db)
        return SourceCodeResponseSchema(
            source_code_id=source_code.id,
            source_code=source_code.source_code,
            user_id=source_code.user_id,
            problem_id=source_code.problem_id,
            status=source_code.status,
            submit_time=source_code.submit_time,
            score=source_code.score,
            verdict=source_code.verdict,
            message=output.get('message', None)
        )
    except Exception as e:
        print(e)
        raise e