from pydantic import BaseModel, EmailStr, Field, conint
from typing import Optional

class AdminTodoResponse(BaseModel):
    id: int
    title: str = Field(..., min_length=3, max_length=100, description="O título deve ter entre 3 e 100 caracteres.")
    description: str = Field(..., min_length=5, max_length=500, description="A descrição deve ter entre 5 e 500 caracteres.")
    priority: int = Field(..., ge=1, le=5, description="A prioridade deve estar entre 1 (baixa) e 5 (alta).")
    complete: bool
    owner_id: int

    class Config:
        from_attributes = True

class AdminUserResponse(BaseModel):
    id: int
    email: EmailStr = Field(..., description="Deve ser um e-mail válido.")
    username: str = Field(..., min_length=3, max_length=20, pattern="^[a-zA-Z0-9_-]+$", description="O nome de usuário deve ter entre 3 e 20 caracteres e pode conter letras, números, '_' e '-'.")
    first_name: Optional[str] = Field(None, min_length=2, max_length=50, description="O primeiro nome deve ter entre 2 e 50 caracteres.")
    last_name: Optional[str] = Field(None, min_length=2, max_length=50, description="O sobrenome deve ter entre 2 e 50 caracteres.")
    role: str = Field(..., pattern="^(admin|user)$", description="O papel do usuário deve ser 'admin' ou 'user'.")

    class Config:
        from_attributes = True
