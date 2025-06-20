from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .models import StatusEnum, PriorityEnum

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: StatusEnum
    priority: PriorityEnum

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[StatusEnum] = None
    priority: Optional[PriorityEnum] = None

class TaskOut(TaskBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
