from fastapi import APIRouter, HTTPException, status, Depends
from typing import Annotated
from app.schemas.component_schemas import ComponentCreate, ComponentOutResponse, ComponentUpdate
from app.services import component_services
from app.database import get_db
from sqlalchemy.orm import Session
from uuid import UUID

router = APIRouter(prefix="/api/v1/components", tags=["components"])

SessionDep = Annotated[Session, Depends(get_db)]

@router.get("/", response_model=list[ComponentOutResponse]) #JSON array so Python converts it to a list (returns multiple components)
def get_components(db: SessionDep, limit: int = 2, offset: int = 0, status: str | None = None, priority: str | None = None):
    return component_services.get_components(db, limit, offset, status, priority)

@router.post("/", response_model=ComponentOutResponse, status_code=status.HTTP_201_CREATED) #returns a single component not a list or anything
def create_components(payload: ComponentCreate, db: SessionDep):
    """Create a new component"""
    return component_services.create_component(payload, db)
    

@router.get("/{comp_name}", response_model=ComponentOutResponse)
def get_component(comp_name: UUID, db: SessionDep):
    """Retrieves a specific component given its ID"""
    comp = component_services.get_component(comp_name, db)
    if comp is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Component not found")
    return comp

@router.put("/{comp_name}", response_model=ComponentOutResponse)
def update_component(comp_name: UUID, payload: ComponentUpdate, db: SessionDep):
    """Update an existing component"""
    updated_issue = component_services.update_component(comp_name, payload, db)
    if updated_issue is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Component not found")
    return updated_issue

@router.delete("/{comp_name}", status_code=status.HTTP_204_NO_CONTENT)
def delete_component(comp_name: UUID, db: SessionDep):
    """Delete a component given its ID"""
    if not component_services.delete_component(comp_name, db):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Component not found")
    return

