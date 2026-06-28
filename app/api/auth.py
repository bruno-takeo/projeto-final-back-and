from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.usuario import LoginRequest, LoginResponse
from app.services.auth_service import autenticar_usuario

router = APIRouter(
    prefix="/auth",
    tags=["Autenticação"]
)


@router.post("/login", response_model=LoginResponse)
def login(dados_login: LoginRequest, db: Session = Depends(get_db)):
    token = autenticar_usuario(db, dados_login)

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="E-mail ou senha inválidos."
        )

    return {
        "access_token": token,
        "token_type": "Bearer"
    }