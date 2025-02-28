from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.auth.google_auth import get_current_user
from app.database.config import get_db
from app.database.models.problem import Problem
from app.database.schemas.generic_response import GenericResponse
from app.services.source_code import SourceCodeService
from app.database.schemas.source_code import SourceCodeRequestSchema, SourceCodeResponseSchema, TestCaseSampleSchema
from app.services.problem import ProblemService

sourceCodeRouter = APIRouter()

@sourceCodeRouter.post('/submit', response_model=GenericResponse[SourceCodeResponseSchema])
async def create_source_code(source_code_request: SourceCodeRequestSchema, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    """API nhận source code và trả về kết quả chạy mã nguồn bằng C compiler."""
    try:
        problem: Problem = ProblemService(db).get_by_id(source_code_request.problem_id)
        source_code, output = await SourceCodeService(db).create_submission(source_code_request, problem, user['sub'])

        verdict = source_code.verdict
        examples: List[TestCaseSampleSchema] = []
        if len(verdict) > 0:
            for testcase in problem.testcase:
                if testcase['is_example']:
                    verdict_item = next((v for v in verdict if v['testcase_id'] == testcase['id']), None)
                    examples.append(TestCaseSampleSchema(
                        testcode=testcase.get('testcode', None),
                        input=testcase.get('input', ''),
                        expected_output=testcase['output'],
                        output=verdict_item.get('output', ''),
                        is_correct=verdict_item['status']
                    ))
        
        source_code =  SourceCodeResponseSchema(
            source_code_id=source_code.id,
            source_code=source_code.source_code,
            user_id=source_code.user_id,
            problem_id=source_code.problem_id,
            status=source_code.status,
            score=source_code.score,
            test_case_sample=examples,
            message=output.message
        )

        return GenericResponse(data=source_code)
    except Exception as e:
        raise e