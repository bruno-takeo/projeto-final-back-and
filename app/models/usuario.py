from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Enum, Integer, String

from app.db.database import Base
from app.models.enums import PerfilUsuario


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(120), nullable=False)
    email = Column(String(120), unique=True, index=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)
    perfil = Column(Enum(PerfilUsuario), nullable=False, default=PerfilUsuario.CLIENTE)
    consentimento_lgpd = Column(Boolean, nullable=False, default=False)
    ativo = Column(Boolean, nullable=False, default=True)
    data_criacao = Column(DateTime, default=datetime.utcnow)