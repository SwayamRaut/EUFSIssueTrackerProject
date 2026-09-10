import uuid
from app.schemas.issue_schemas import IssueCreate, IssueUpdate, IssueStatus
from sqlalchemy.orm import Session
from sqlalchemy import select
from uuid import UUID
from app.models import Issue

def create_issues(payload: IssueCreate, db: Session):
    """Create a new issue"""
    new_issue = Issue(
        id = uuid.uuid4(),
        title = payload.title,
        description = payload.description,
        priority = payload.priority,
        status = IssueStatus.open
     ) #this variable is a new Issue instantiation
    db.add(new_issue)
    db.commit()
    db.refresh(new_issue)
    return new_issue

def get_issues(db: Session, limit: int = 2, offset: int = 3, status: str | None = None, priority: str | None = None):
    """Retrieve all issues"""
    stmt = select(Issue).limit(limit).offset(offset)
    if status is not None:
        stmt = stmt.where(Issue.status==status)
    if priority is not None:
        stmt = stmt.where(Issue.priority==priority)
    issues = db.scalars(stmt).all()
    return issues

def get_issue(issue_id: UUID, db: Session):
    issue = db.get(Issue, issue_id)
    return issue


def update_issue(issue_id: UUID, payload: IssueUpdate, db: Session):
    """Update an existing issue"""
    issue = db.get(Issue, issue_id)
    if issue is None:
        return None
    
    if payload.title is not None:
        issue.title = payload.title
    if payload.description is not None:
        issue.description = payload.description
    if payload.priority is not None:
        issue.priority = payload.priority
    if payload.status is not None:
        issue.status = payload.status
    db.commit()
    db.refresh(issue)
    return issue

def delete_issue(issue_id: UUID, db: Session):
    """Delete an issue given its ID"""
    issue = db.get(Issue, issue_id)
    if issue is None:
        return None
    db.delete(issue)
    db.commit()
    return True