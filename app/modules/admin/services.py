from sqlalchemy.orm import Session
from app.modules.todos.models import Todos
from app.modules.users.models import Users
from fastapi import HTTPException, status

def get_all_todos(db: Session):
    return db.query(Todos).all()

def get_all_users(db: Session):
    return db.query(Users).all()

def delete_todo(db: Session, todo_id: int):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found.")
    
    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()

def delete_user(db: Session, user_id: int):
    user_model = db.query(Users).filter(Users.id == user_id).first()
    if user_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    
    db.query(Users).filter(Users.id == user_id).delete()
    db.commit()
