from datetime import datetime, timedelta, timezone

from jose import jwt

SECRET_KEY = "chave-secreta-projeto-final-raizes-nordeste"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def criar_token_acesso(data: dict) -> str:
    dados = data.copy()
    expiracao = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    dados.update({"exp": expiracao})
    return jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)