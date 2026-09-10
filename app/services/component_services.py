from app.schemas.component_schemas import ComponentCreate, ComponentUpdate
from sqlalchemy.orm import Session, selectinload
from sqlalchemy import select
from app.models import Component
from uuid import UUID

def create_component(payload: ComponentCreate, db: Session):
    """Create a new component"""
    new_comp = Component(
        name = payload.name,
        type = payload.type,
        cost = "unknown"
    )
    db.add(new_comp)
    db.commit()
    db.refresh(new_comp)
    return new_comp

def get_components(db: Session, limit: int = 2, offset: int = 0, status: str | None = None, priority: str | None = None):
    """Get all components"""
    stmt = select(Component).limit(limit).offset(offset)
    if status is not None:
        stmt = stmt.where(Component.status==status)
    if priority is not None:
        stmt = stmt.where(Component.priority==priority)
    components = db.scalars(stmt).all()
    return components

def get_component(comp_name: UUID, db: Session):
    """Retrieve a component given its name"""
    component = db.get(Component, comp_name)
    if(component is not None):
        return component
    
    #We are now going to only print out all the issues with the given components
    #We use eager loading to avoid N+1 problem because by default SQLAlchemy performs lazy loading
    #which means to avoid unnecessary database work upfront, it does not load all of the content until explicitly accessed
    stmt = select(Component).options(selectinload(Component.issues))
    components = db.scalars(stmt).all()
    for comp in components:
        for issue in comp.issues:
            print(issue.title)
    return None

def update_component(comp_name: UUID, payload: ComponentUpdate, db: Session):
    """Update an existing component"""
    component = db.get(Component, comp_name)
    if component is None:
        return None
    
    if payload.name is not None:
        component.name = payload.name
    if payload.type is not None:
        component.type = payload.type
    if payload.cost is not None:
        component.cost = payload.cost

    db.commit()
    db.refresh(component)
    return component

def delete_component(comp_name: UUID, db: Session):
    component = db.get(Component, comp_name)
    if component is None:
        return False
    db.delete(component)
    db.commit()

    return True