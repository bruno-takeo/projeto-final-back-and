from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.usuario import Usuario
from app.schemas.estoque import EstoqueCreate, EstoqueResponse
from app.security.dependencies import obter_usuario_logado, exigir_admin
from app.services.estoque_service import criar_estoque, listar_estoques

router = APIRouter(
    prefix="/estoques",
    tags=["Estoques"]
)


@router.post("/", response_model=EstoqueResponse, status_code=status.HTTP_201_CREATED)
def cadastrar_estoque(
    estoque: EstoqueCreate,
    db: Session = Depends(get_db),
    usuario_logado: Usuario = Depends(exigir_admin)
):
    try:
        return criar_estoque(db, estoque)
    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )


@router.get("/", response_model=list[EstoqueResponse])
def consultar_estoques(
    db: Session = Depends(get_db),
    usuario_logado: Usuario = Depends(obter_usuario_logado)
):
    return listar_estoques(db)