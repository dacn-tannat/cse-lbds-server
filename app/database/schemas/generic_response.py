from pydantic import BaseModel, Field
from typing import Generic, TypeVar, Optional

T = TypeVar('T')

class GenericResponse(BaseModel, Generic[T]):
    code: int = Field(default=0, example=0)
    msg: str = Field(default="success", example="success")
    data: Optional[T]