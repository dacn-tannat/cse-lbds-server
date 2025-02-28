from typing import List, Optional
from pydantic import BaseModel

class SourceCodeRequestSchema(BaseModel):
    source_code: str
    problem_id: int

class SourceCodeResponseSchema(BaseModel):
    source_code_id: int
    source_code: str
    user_id: int
    problem_id: int
    status: int
    score: float
    test_case_sample: List['TestCaseSampleSchema']
    message: str

class TestCaseSampleSchema(BaseModel):
    input: Optional[str]
    testcode: Optional[str]
    output: str
    expected_output: str
    is_correct: bool

class SourceCodeSubmitResponseSchema(BaseModel):
    status: int
    score: float
    message: str
    verdict: List[object]