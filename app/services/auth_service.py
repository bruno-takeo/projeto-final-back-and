from sqlalchemy.orm import Session

from app.models.usuario import Usuario
from app.schemas.usuario import LoginRequest
from app.security.jwt import criar_token_acesso
from app.security.password import verificar_senha


def autenticar_usuario(db: Session, login: LoginRequest):
    usuario = db.query(Usuario).filter(Usuario.email == login.email).first()

    if not usuario:
        return None

    if not verificar_senha(login.senha, usuario.senha_hash):
        return None

    token = criar_token_acesso(
        {
            "sub": usuario.email,
            "perfil": usuario.perfil.value,
            "usuario_id": usuario.id,
        }
    )

    return token