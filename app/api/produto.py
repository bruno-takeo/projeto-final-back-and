from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.usuario import Usuario
from app.schemas.produto import ProdutoCreate, ProdutoResponse
from app.security.dependencies import obter_usuario_logado, exigir_admin
from app.services.produto_service import criar_produto, listar_produtos

router = APIRouter(
    prefix="/produtos",
    tags=["Produtos"]
)


@router.post("/", response_model=ProdutoResponse, status_code=status.HTTP_201_CREATED)
def cadastrar_produto(
    produto: ProdutoCreate,
    db: Session = Depends(get_db),
    usuario_logado: Usuario = Depends(exigir_admin)
):
    return criar_produto(db, produto)


@router.get("/", response_model=list[ProdutoResponse])
def consultar_produtos(
    db: Session = Depends(get_db),
    usuario_logado: Usuario = Depends(obter_usuario_logado)
):
    return listar_produtos(db)