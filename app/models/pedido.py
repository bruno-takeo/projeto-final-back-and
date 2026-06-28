from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db.database import Base
from app.models.enums import CanalPedido, StatusPedido


class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    unidade_id = Column(Integer, ForeignKey("unidades.id"), nullable=False)
    canal_pedido = Column(Enum(CanalPedido), nullable=False)
    status = Column(
        Enum(StatusPedido),
        nullable=False,
        default=StatusPedido.AGUARDANDO_PAGAMENTO
    )
    valor_total = Column(Float, nullable=False, default=0.0)
    data_pedido = Column(DateTime, default=datetime.utcnow)

    cliente = relationship("Usuario")
    unidade = relationship("Unidade")
    itens = relationship("ItemPedido", back_populates="pedido")
    pagamento = relationship("Pagamento", back_populates="pedido", uselist=False)