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
    submit_time: str
    score: int
    verdict: str
    message: str