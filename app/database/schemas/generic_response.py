from pydantic import BaseModel, Field
from typing import Generic, TypeVar, Optional

T = TypeVar('T')

class GenericResponse(BaseModel, Generic[T]):
    detail: str = Field(default="success", example="success")
    data: Optional[T]