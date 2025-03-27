from pydantic import BaseModel, Field
from app.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean


class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_lenght = 6)

class Token(BaseModel):
    access_token: str
    token_type: str
