#rules of how data should look and be formatted in
from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

class IssueStatus(str, Enum):
    open = "open"
    in_progress = "in_progress"
    closed = "closed"

class IssuePriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class IssueCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=5, max_length=1000)
    priority: IssuePriority = IssuePriority.medium #sets default priority to medium

class IssueUpdate(BaseModel):
    title: Optional[str] = Field(default=None, max_length=100)
    description: Optional[str] = Field(default=None, max_length=1000)
    priority: Optional[IssuePriority] = None
    status: Optional[IssueStatus] = None

#We also need a schema for issue out response
class IssueOut(BaseModel):
    id: UUID
    title: str
    description: str
    priority: IssuePriority
    status: IssueStatus

    """
    The from_attributes = True tells Pydantic 
    "when given an object instead of a dict, read the fields from attributes." 
    Without it, FastAPI can't convert your SQLAlchemy Issue into an IssueOut response.    
    """

    model_config = {"from_attributes": True} # allows reading from ORM objects
