from sqlalchemy.orm import Session

from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate


def criar_usuario(db: Session, usuario: UsuarioCreate) -> Usuario:
    usuario_existente = db.query(Usuario).filter(Usuario.email == usuario.email).first()

    if usuario_existente:
        raise ValueError("E-mail já cadastrado.")

    novo_usuario = Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha_hash=usuario.senha,
        perfil=usuario.perfil,
        consentimento_lgpd=usuario.consentimento_lgpd,
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario