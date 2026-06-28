from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr

from app.models.enums import PerfilUsuario


class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    perfil: PerfilUsuario = PerfilUsuario.CLIENTE
    consentimento_lgpd: bool


class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr
    perfil: PerfilUsuario
    consentimento_lgpd: bool
    ativo: bool
    data_criacao: datetime

    model_config = ConfigDict(from_attributes=True)


class LoginRequest(BaseModel):
    email: EmailStr
    senha: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "Bearer"