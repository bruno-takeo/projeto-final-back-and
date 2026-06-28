from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base
from app.models.enums import FormaPagamento, StatusPagamento


class Pagamento(Base):
    __tablename__ = "pagamentos"

    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"), nullable=False, unique=True)
    forma_pagamento = Column(Enum(FormaPagamento), nullable=False, default=FormaPagamento.MOCK)
    status_pagamento = Column(Enum(StatusPagamento), nullable=False, default=StatusPagamento.PENDENTE)
    valor = Column(Float, nullable=False)
    codigo_transacao_mock = Column(String(100), nullable=True)
    mensagem = Column(String(255), nullable=True)
    data_pagamento = Column(DateTime, default=datetime.utcnow)

    pedido = relationship("Pedido", back_populates="pagamento")