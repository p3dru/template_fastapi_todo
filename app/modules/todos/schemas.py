from typing import Optional
from pydantic import BaseModel, Field

class TodoRequest(BaseModel):
    title: str = Field(..., min_length=3, max_length=50, description="Título deve ter entre 3 e 50 caracteres.")
    description: str = Field(..., min_length=3, max_length=100, description="A descrição deve ter entre 3 e 100 caracteres.")
    priority: int = Field(..., gt=0, lt=6, description="A prioridade deve ser um número entre 1 e 5.")
    complete: bool = Field(..., description="Indica se a tarefa está concluída.")

    class Config:
        from_attributes = True

class TodoUpdateRequest(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=50, description="Título deve ter entre 3 e 50 caracteres.")
    description: Optional[str] = Field(None, min_length=3, max_length=100, description="A descrição deve ter entre 3 e 100 caracteres.")
    priority: Optional[int] = Field(None, gt=0, lt=6, description="A prioridade deve ser um número entre 1 e 5.")
    complete: Optional[bool] = Field(None, description="Indica se a tarefa está concluída.")

    class Config:
        from_attributes = True