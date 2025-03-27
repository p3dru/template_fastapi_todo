from fastapi import APIRouter, Depends, HTTPException, Path
from app.database import get_db
from app.modules.auth.dependencies import get_current_user
from .services import get_all_todos, get_all_users, delete_todo, delete_user
from sqlalchemy.orm import Session
from starlette import status
from typing import Annotated
from .schemas import AdminTodoResponse, AdminUserResponse

router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

def is_admin(user: dict):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not an admin")

@router.get("/todos", response_model=list[AdminTodoResponse], status_code=status.HTTP_200_OK)
async def read_all_todos(user: user_dependency, db: db_dependency):
    is_admin(user)
    return get_all_todos(db)

@router.get("/users", response_model=list[AdminUserResponse], status_code=status.HTTP_200_OK)
async def read_all_users(user: user_dependency, db: db_dependency):
    is_admin(user)
    return get_all_users(db)

@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo_admin(
    user: user_dependency, 
    db: db_dependency,
    todo_id: int = Path(gt=0)
    ):
    is_admin(user)
    delete_todo(db, todo_id)

@router.delete("/user/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_admin(user: user_dependency, db: db_dependency, user_id: int = Path(gt=0)):
    is_admin(user)
    delete_user(db, user_id)
