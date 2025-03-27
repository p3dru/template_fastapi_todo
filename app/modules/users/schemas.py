from pydantic import BaseModel, Field, EmailStr
from typing import Literal, Optional

class CreateUserRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=20, description="O nome de usuário deve ter entre 3 e 20 caracteres.")
    email: EmailStr = Field(..., description="Deve ser um e-mail válido.")
    first_name: str = Field(..., min_length=2, max_length=30, description="O primeiro nome deve ter entre 2 e 30 caracteres.")
    last_name: str = Field(..., min_length=2, max_length=30, description="O sobrenome deve ter entre 2 e 30 caracteres.")
    password: str = Field(..., min_length=6, max_length=100, description="A senha deve ter pelo menos 6 caracteres.")
    role: Literal["admin", "user"] = Field(..., description="O papel do usuário pode ser 'admin' ou 'user'.")

    class Config:
        from_attributes = True

class UserVerification(BaseModel):
    password: str = Field(..., min_length=6, max_length=100, description="A senha atual deve ter pelo menos 6 caracteres.")
    new_password: str = Field(..., min_length=6, max_length=100, description="A nova senha deve ter pelo menos 6 caracteres.")

    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr  # Garantindo que o e-mail seja válido
    first_name: str
    last_name: str
    role: Literal["admin", "user"]  # Garantindo que o papel seja apenas "admin" ou "user"

    class Config:
        from_attributes = True