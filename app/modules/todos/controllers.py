from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from starlette import status
from app.database import get_db
from app.modules.auth.dependencies import get_current_user
from .services import get_all_todos, get_todo, create_new_todo, update_existing_todo, delete_existing_todo
from .schemas import TodoRequest, TodoUpdateRequest

router = APIRouter(prefix="/todos", tags=["todos"])

db_dependency = Depends(get_db)
user_dependency = Depends(get_current_user)

@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(user: dict = user_dependency, db: Session = db_dependency):
    return get_all_todos(db, user)

@router.get("/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(user: dict = user_dependency, db: Session = db_dependency, todo_id: int = Path(gt=0)):
    return get_todo(db, user, todo_id)

@router.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(user: dict = user_dependency, db: Session = db_dependency, todo_request: TodoRequest = Depends()):
    return create_new_todo(db, user, todo_request)

@router.put('/todo/{todo_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(user: dict = user_dependency, db: Session = db_dependency, todo_request: TodoUpdateRequest = Depends(), todo_id: int = Path(gt=0)):
    return update_existing_todo(db, user, todo_request, todo_id)

@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: dict = user_dependency, db: Session = db_dependency, todo_id: int = Path(gt=0)):
    return delete_existing_todo(db, user, todo_id)
