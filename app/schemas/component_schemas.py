#rules of how data should look and be formatted in
from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID


class ComponentType(str, Enum):
    unknown = "unknown"
    suspension = "suspension"
    electronics = "electronics"
    telemetry = "telemetry"
    powertrain = "powertrain"
    aero = "aero"

class ComponentCost(str, Enum):
    cheap = "cheap"
    normalPrice = "normal price"
    expensive = "expensive"
    unknown = "unknown"

class ComponentCreate(BaseModel):
    name: UUID
    type: ComponentType = ComponentType.unknown

class ComponentUpdate(BaseModel):
    name: Optional[UUID] = None
    type: Optional[ComponentType] = None
    cost: Optional[ComponentCost] = None

class ComponentOutResponse(BaseModel):
    name: UUID
    type: ComponentType
    cost: ComponentCost

model_config = {"from_attributes": True} # allows reading from ORM objects