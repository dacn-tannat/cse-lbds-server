from typing import List
from pydantic import BaseModel

class BugCheckRequestSchema(BaseModel):
    prediction_id: int
    position: List[int]