from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.modules.todos.models import Todos
from app.modules.todos.schemas import TodoRequest

def get_all_todos(db: Session, user: dict):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    return db.query(Todos).filter(Todos.owner_id == user.get('id')).all()

def get_todo(db: Session, user: dict, todo_id: int):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    
    todo_model = db.query(Todos).filter(Todos.id == todo_id, Todos.owner_id == user.get('id')).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    return todo_model

def create_new_todo(db: Session, user: dict, todo_request: TodoRequest):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    
    todo_model = Todos(**todo_request.model_dump(), owner_id=user.get('id'))

    db.add(todo_model)
    db.commit()
    db.refresh(todo_model)
    return todo_model

def update_existing_todo(db: Session, user: dict, todo_request: TodoRequest, todo_id: int):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    
    todo_model = db.query(Todos).filter(Todos.id == todo_id, Todos.owner_id == user.get('id')).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found.")

    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.commit()
    return {"message": "Todo updated successfully"}

def delete_existing_todo(db: Session, user: dict, todo_id: int):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")

    todo_model = db.query(Todos).filter(Todos.id == todo_id, Todos.owner_id == user.get('id')).first()
    
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    db.delete(todo_model)
    db.commit()
    return {"message": "Todo deleted successfully"}
