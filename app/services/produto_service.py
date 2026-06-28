from sqlalchemy.orm import Session

from app.models.produto import Produto
from app.schemas.produto import ProdutoCreate


def criar_produto(db: Session, produto: ProdutoCreate) -> Produto:
    novo_produto = Produto(
        nome=produto.nome,
        descricao=produto.descricao,
        preco=produto.preco,
        categoria=produto.categoria,
        ativo=produto.ativo,
    )

    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)

    return novo_produto


def listar_produtos(db: Session) -> list[Produto]:
    return db.query(Produto).filter(Produto.ativo == True).all()