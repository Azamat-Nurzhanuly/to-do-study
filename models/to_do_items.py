from typing import Optional

from pydantic import BaseModel


class ToDoItemAdd(BaseModel):
    name: str
    description: Optional[str] = None


class ToDoItem(ToDoItemAdd):
    id: int
