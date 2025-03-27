from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from jose import jwt
import os
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from app.modules.users.models import Users

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def authenticate_user(username: str, password: str, db: Session):
    user = db.query(Users).filter(Users.username == username).first()

    if not user or not bcrypt_context.verify(password, user.hashed_password):
        return None

    return user

def create_access_token(username: str, user_id: int, role: str, expire_delta: timedelta):
    encode = {'sub': username, 'id': user_id, 'role': role}
    expires = datetime.now(timezone.utc) + expire_delta

    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
