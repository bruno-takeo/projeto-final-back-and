from sqlalchemy.orm import Session

from app.models.unidade import Unidade
from app.schemas.unidade import UnidadeCreate


def criar_unidade(db: Session, unidade: UnidadeCreate) -> Unidade:
    nova_unidade = Unidade(
        nome=unidade.nome,
        cidade=unidade.cidade,
        estado=unidade.estado,
        ativa=unidade.ativa,
    )

    db.add(nova_unidade)
    db.commit()
    db.refresh(nova_unidade)

    return nova_unidade


def listar_unidades(db: Session) -> list[Unidade]:
    return db.query(Unidade).filter(Unidade.ativa == True).all()