from pydantic import BaseModel
from typing import Optional

class AdminTodoResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: int
    complete: bool
    owner_id: int

    class Config:
        from_attributes = True

class AdminUserResponse(BaseModel):
    id: int
    email: str
    username: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: str
    phone_number: Optional[str] = None

    class Config:
        from_attributes = True
