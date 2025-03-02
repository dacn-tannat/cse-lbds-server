from enum import Enum
from typing import List
from pydantic import BaseModel


class BugCheckType(Enum):
    TOKEN_ERROR = 'TOKEN_ERROR'
    SUGGESTION_USEFUL = 'SUGGESTION_USEFUL'

class BugCheckRequestSchema(BaseModel):
    prediction_id: int
    type: BugCheckType
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
    line_number: int
    is_token_error: bool
    is_suggestion_useful: bool
