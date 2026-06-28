import uuid

from sqlalchemy.orm import Session

from app.models.enums import (
    FormaPagamento,
    StatusPagamento,
    StatusPedido,
)
from app.models.pagamento import Pagamento
from app.models.pedido import Pedido
from app.schemas.pagamento import PagamentoCreate


def processar_pagamento(
    db: Session,
    pedido_id: int,
    pagamento: PagamentoCreate,
):

    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()

    if not pedido:
        raise ValueError("Pedido não encontrado.")

    pagamento_existente = (
        db.query(Pagamento)
        .filter(Pagamento.pedido_id == pedido_id)
        .first()
    )

    if pagamento_existente:
        raise ValueError("Pedido já possui pagamento.")

    status_pagamento = (
        StatusPagamento.APROVADO
        if pagamento.aprovado
        else StatusPagamento.RECUSADO
    )

    pedido.status = (
        StatusPedido.PAGO
        if pagamento.aprovado
        else StatusPedido.CANCELADO
    )

    novo_pagamento = Pagamento(
        pedido_id=pedido.id,
        forma_pagamento=FormaPagamento.MOCK,
        status_pagamento=status_pagamento,
        valor=pedido.valor_total,
        codigo_transacao_mock=str(uuid.uuid4()),
        mensagem="Pagamento simulado com sucesso."
        if pagamento.aprovado
        else "Pagamento recusado.",
    )

    db.add(novo_pagamento)
    db.commit()
    db.refresh(novo_pagamento)

    return novo_pagamento