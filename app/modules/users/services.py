from sqlalchemy.orm import Session
from fastapi import HTTPException
from passlib.context import CryptContext
from .models import Users
from .schemas import UserVerification


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(db: Session, user: dict):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    return db.query(Users).filter(Users.id == user.get("id")).first()

def change_password(db: Session, user: dict, user_verification: UserVerification):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    
    user_model = db.query(Users).filter(Users.id == user.get("id")).first()
    if not user_model or not bcrypt_context.verify(user_verification.password, user_model.hashed_password):
        raise HTTPException(status_code=401, detail="Error on password change")
    
    user_model.hashed_password = bcrypt_context.hash(user_verification.new_password)
    db.commit()
    return {"message": "Password changed successfully"}

def change_phone_number(db: Session, user: dict, phone_number: str):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    
    user_model = db.query(Users).filter(Users.id == user.get("id")).first()
    if not user_model:
        raise HTTPException(status_code=404, detail="User not found")

    user_model.phone_number = phone_number
    db.commit()
    return {"message": "Phone number updated successfully"}