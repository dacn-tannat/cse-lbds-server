from pydantic import BaseModel

class SourceCodeRequestSchema(BaseModel):
    source_code: str
    problem_id: int