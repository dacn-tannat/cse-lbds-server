from typing import Optional
from pydantic import BaseModel


class ProblemResponseSchema(BaseModel):
    id: int
    name: str
    category: Optional[str] = None
    lab_id: Optional[int] = None
    is_active: bool
    description: str
    constrain: list[str]
    examples: list['TestCaseSchema']

class TestCaseSchema(BaseModel):
    input: str
    output: str

class ProblemOverviewResponseSchema(BaseModel):
    id: int
    name: str
    category: Optional[str] = None
    lab_id: Optional[int] = None
    is_active: bool