from sqlalchemy.orm import Session

from app.models.estoque import Estoque
from app.models.produto import Produto
from app.models.unidade import Unidade
from app.schemas.estoque import EstoqueCreate


def criar_estoque(db: Session, estoque: EstoqueCreate) -> Estoque:
    unidade = db.query(Unidade).filter(Unidade.id == estoque.unidade_id).first()
    produto = db.query(Produto).filter(Produto.id == estoque.produto_id).first()

    if not unidade:
        raise ValueError("Unidade não encontrada.")

    if not produto:
        raise ValueError("Produto não encontrado.")

    estoque_existente = (
        db.query(Estoque)
        .filter(
            Estoque.unidade_id == estoque.unidade_id,
            Estoque.produto_id == estoque.produto_id
        )
        .first()
    )

    if estoque_existente:
        estoque_existente.quantidade += estoque.quantidade
        db.commit()
        db.refresh(estoque_existente)
        return estoque_existente

    novo_estoque = Estoque(
        unidade_id=estoque.unidade_id,
        produto_id=estoque.produto_id,
        quantidade=estoque.quantidade,
    )

    db.add(novo_estoque)
    db.commit()
    db.refresh(novo_estoque)

    return novo_estoque


def listar_estoques(db: Session) -> list[Estoque]:
    return db.query(Estoque).all()