from pydantic import BaseModel, constr
from uuid import UUID
from .enums import Status


class TaskEntry(BaseModel):
    title: constr(min_length=3, max_length=50)
    description: constr(max_length=140)
    status: Status = Status.in_progress

class Task(TaskEntry):
    id: UUID
