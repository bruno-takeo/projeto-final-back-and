from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.models.enums import FormaPagamento, StatusPagamento


class PagamentoCreate(BaseModel):
    aprovado: bool


class PagamentoResponse(BaseModel):
    id: int
    pedido_id: int
    forma_pagamento: FormaPagamento
    status_pagamento: StatusPagamento
    valor: float
    codigo_transacao_mock: str | None
    mensagem: str | None
    data_pagamento: datetime

    model_config = ConfigDict(from_attributes=True)