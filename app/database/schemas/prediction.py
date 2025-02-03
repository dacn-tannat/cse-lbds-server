from typing import List
from pydantic import BaseModel

class PredictionResponseSchema(BaseModel):
    id: int
    source_code_id: int
    positions: List['BuggyPosition']

class BuggyPosition(BaseModel):
    id: int
    start_index: int
    position: int
    original_token: str
    predicted_token: str