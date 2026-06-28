from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.models.enums import CanalPedido, StatusPedido


class ItemPedidoCreate(BaseModel):
    produto_id: int
    quantidade: int


class PedidoCreate(BaseModel):
    unidade_id: int
    canal_pedido: CanalPedido
    itens: list[ItemPedidoCreate]


class ItemPedidoResponse(BaseModel):
    id: int
    produto_id: int
    quantidade: int
    preco_unitario: float

    model_config = ConfigDict(from_attributes=True)


class PedidoResponse(BaseModel):
    id: int
    cliente_id: int
    unidade_id: int
    canal_pedido: CanalPedido
    status: StatusPedido
    valor_total: float
    data_pedido: datetime
    itens: list[ItemPedidoResponse]

    model_config = ConfigDict(from_attributes=True)