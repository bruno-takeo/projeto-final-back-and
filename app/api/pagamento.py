from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.usuario import Usuario
from app.schemas.pagamento import (
    PagamentoCreate,
    PagamentoResponse,
)
from app.security.dependencies import obter_usuario_logado
from app.services.pagamento_service import processar_pagamento

router = APIRouter(
    prefix="/pagamentos",
    tags=["Pagamentos"],
)


@router.post(
    "/{pedido_id}",
    response_model=PagamentoResponse,
)
def pagar_pedido(
    pedido_id: int,
    pagamento: PagamentoCreate,
    db: Session = Depends(get_db),
    usuario_logado: Usuario = Depends(obter_usuario_logado),
):
    try:
        return processar_pagamento(
            db,
            pedido_id,
            pagamento,
        )

    except ValueError as erro:
        raise HTTPException(
            status_code=409,
            detail=str(erro),
        )