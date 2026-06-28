from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.usuario import UsuarioCreate, UsuarioResponse
from app.services.usuario_service import criar_usuario
from app.models.usuario import Usuario
from app.security.dependencies import obter_usuario_logado

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuários"]
)


@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def cadastrar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    try:
        return criar_usuario(db, usuario)
    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(erro)
        )
    
@router.get("/me", response_model=UsuarioResponse)
def consultar_meu_usuario(usuario_logado: Usuario = Depends(obter_usuario_logado)):
    return usuario_logado