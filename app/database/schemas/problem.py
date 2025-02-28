from typing import Optional
from pydantic import BaseModel


class ProblemResponseSchema(BaseModel):
    id: int
    name: str
    category: Optional[str] = None
    lab_id: Optional[str] = None
    is_active: bool
    description: str
    constrain: Optional[list[str]]
    examples: list['TestCaseSchema']

class TestCaseSchema(BaseModel):
    input: Optional[str]
    testcode: Optional[str]
    output: str

class ProblemOverviewResponseSchema(BaseModel):
    id: int
    name: str
    category: Optional[str] = None
    lab_id: Optional[str] = None
    is_active: bool