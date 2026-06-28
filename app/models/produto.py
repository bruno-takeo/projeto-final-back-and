from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String

from app.db.database import Base


class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(120), nullable=False)
    descricao = Column(String(255), nullable=True)
    preco = Column(Float, nullable=False)
    categoria = Column(String(80), nullable=False)
    ativo = Column(Boolean, nullable=False, default=True)
    data_criacao = Column(DateTime, default=datetime.utcnow)