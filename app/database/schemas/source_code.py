from datetime import datetime
from typing import List
from pydantic import BaseModel

class SourceCodeRequestSchema(BaseModel):
    source_code: str
    problem_id: int

class SourceCodeResponseSchema(BaseModel):
    source_code_id: int
    source_code: str
    user_id: str
    problem_id: int
    status: int
    score: float
    test_case_sample: List['TestCaseSchema']
    message: str

class TestCaseSchema(BaseModel):
    input: str
    output: str
    is_correct: bool