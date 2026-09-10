from pydantic import BaseModel, Field
from typing import Any

class ErrorDetail(BaseModel):
    code: str
    message: str
    details: Any | None = None

class ErrorResponse(BaseModel):
    error: ErrorDetail