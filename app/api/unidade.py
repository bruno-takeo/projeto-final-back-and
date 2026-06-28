from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.usuario import Usuario
from app.schemas.unidade import UnidadeCreate, UnidadeResponse
from app.security.dependencies import obter_usuario_logado, exigir_admin
from app.services.unidade_service import criar_unidade, listar_unidades

router = APIRouter(
    prefix="/unidades",
    tags=["Unidades"]
)


@router.post("/", response_model=UnidadeResponse, status_code=status.HTTP_201_CREATED)
def cadastrar_unidade(
    unidade: UnidadeCreate,
    db: Session = Depends(get_db),
    usuario_logado: Usuario = Depends(exigir_admin)
):
    return criar_unidade(db, unidade)


@router.get("/", response_model=list[UnidadeResponse])
def consultar_unidades(
    db: Session = Depends(get_db),
    usuario_logado: Usuario = Depends(obter_usuario_logado)
):
    return listar_unidades(db)