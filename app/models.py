from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID
import uuid
from datetime import datetime
from sqlalchemy import DateTime

from app.database import Base #we import from file instead of defining locally



#Issue class is a subclass of the above user-defined Base class
class Issue(Base):
    __tablename__ = "issues_table"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text)
    priority: Mapped[str] = mapped_column(String(50), default="medium")
    status: Mapped[str] = mapped_column(String(20), default="open", index=True)

    #Foreign key column
    component_name: Mapped[UUID | None] = mapped_column(ForeignKey('components_table.name'))

    #Relationship declaration (bidirectional)
    component: Mapped["Component | None"] = relationship(back_populates="issues")

class Component(Base):
    __tablename__ = "components_table"
    name: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    type: Mapped[str] = mapped_column(String(20), default='unknown')
    cost: Mapped[str] = mapped_column(String(20), default='unknown')
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow) # NEW change to test Alembic workflow

    #Relationship on the other side (bidirectional)
    issues: Mapped[list["Issue"]] = relationship(back_populates="component")