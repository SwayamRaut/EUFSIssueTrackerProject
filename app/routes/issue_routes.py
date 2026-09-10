from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas.issue_schemas import IssueCreate, IssueOut, IssueUpdate
from app.services import issue_services
from sqlalchemy.orm import Session
from typing import Annotated
from app.database import get_db
from uuid import UUID

#We need to add validation to the parameters and the Query will do that automatically preventing like limit=999999. You're telling FastAPI three things:
#limit is a query parameter (from the URL's ?limit=...)
#Its type is int
#It must satisfy: ge=1 (greater or equal to 1) AND le=100 (less or equal to 100)
from fastapi import Query

router = APIRouter(prefix="/api/v1/issues", tags=["issues"])

#Prepare database session injection
SessionDep = Annotated[Session, Depends(get_db)]


@router.get("/", response_model=list[IssueOut]) #JSON array so Python converts it to a list (returns multiple issues)
def get_issues(db: SessionDep, limit: int = Query(default=10, ge=1, le=100), offset: int = Query(default=0, ge=0), status: str | None = None, priority: str | None = None):
    #Above we injected a dependency, parameter of Depends in this case must be a function not its result
    return issue_services.get_issues(db, limit, offset, status, priority)

@router.post("/", response_model=IssueOut, status_code=status.HTTP_201_CREATED) #returns a single issue not a list or anything
def create_issues(payload: IssueCreate, db: SessionDep):
    """Create a new issue"""
    return issue_services.create_issues(payload, db)
    

@router.get("/{issue_id}", response_model=IssueOut)
def get_issue(issue_id: UUID, db: SessionDep):
    """Retrieves a specific issue given its ID"""
    issue = issue_services.get_issue(issue_id, db)
    if issue is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")
    return issue

@router.put("/{issue_id}", response_model=IssueOut)
def update_issue(issue_id: UUID, payload: IssueUpdate, db: SessionDep):
    """Update an existing issue"""
    updated_issue = issue_services.update_issue(issue_id, payload, db)
    if updated_issue is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")
    return updated_issue

@router.delete("/{issue_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_issue(issue_id: UUID, db: SessionDep):
    """Delete an issue given its ID"""
    if not issue_services.delete_issue(issue_id, db):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")
    return

