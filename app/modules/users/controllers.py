from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status
from app.database import get_db
from app.modules.auth.routers import get_current_user
from .services import get_user, change_password, change_phone_number
from .schemas import UserVerification

router = APIRouter(prefix="/user", tags=["user"])

db_dependency = Depends(get_db)
user_dependency = Depends(get_current_user)

@router.get("/", status_code=status.HTTP_200_OK)
async def read_user(user: dict = user_dependency, db: Session = db_dependency):
    return get_user(db, user)

@router.put("/password", status_code=status.HTTP_204_NO_CONTENT)
async def update_password(user: dict = user_dependency, db: Session = db_dependency, user_verification: UserVerification = Depends()):
    return change_password(db, user, user_verification)

@router.put("/phonenumber/{phone_number}", status_code=status.HTTP_204_NO_CONTENT)
async def update_phone_number(phone_number: str, user: dict = user_dependency, db: Session = db_dependency):
    return change_phone_number(db, user, phone_number)
