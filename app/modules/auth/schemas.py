from pydantic import BaseModel, Field


class TokenSchema(BaseModel):
    access_token: str = Field(..., min_length=20, max_length=500, description="O token de acesso deve ter entre 20 e 500 caracteres.")
    token_type: str = Field(..., pattern="^bearer$", description="O tipo de token deve ser 'bearer'.")

    class Config:
        from_attributes = True
