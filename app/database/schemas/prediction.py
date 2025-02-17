from typing import List
from pydantic import BaseModel

from app.database.models.buggy_position import BuggyPosition

class BugCheckRequestSchema(BaseModel):
    prediction_id: int
    position: List[int]

class BugPositionResponseSchema(BaseModel):
    id: int
    model_id: int
    source_code_id: int
    buggy_position: List['BuggyPositionSchema']
    
class BuggyPositionSchema(BaseModel):
    id: int
    position: int
    start_index: int
    original_token: str
    predicted_token: str
    is_used: bool
