from sqlalchemy.orm import Session

from app.models.estoque import Estoque
from app.models.item_pedido import ItemPedido
from app.models.pedido import Pedido
from app.models.produto import Produto
from app.models.unidade import Unidade
from app.models.usuario import Usuario
from app.schemas.pedido import PedidoCreate


def criar_pedido(db: Session, pedido: PedidoCreate, usuario_logado: Usuario) -> Pedido:
    unidade = db.query(Unidade).filter(Unidade.id == pedido.unidade_id, Unidade.ativa == True).first()

    if not unidade:
        raise ValueError("Unidade não encontrada ou inativa.")

    if not pedido.itens:
        raise ValueError("O pedido deve possuir ao menos um item.")

    valor_total = 0.0
    itens_processados = []

    for item in pedido.itens:
        if item.quantidade <= 0:
            raise ValueError("A quantidade dos itens deve ser maior que zero.")

        produto = db.query(Produto).filter(Produto.id == item.produto_id, Produto.ativo == True).first()

        if not produto:
            raise ValueError(f"Produto {item.produto_id} não encontrado ou inativo.")

        estoque = (
            db.query(Estoque)
            .filter(
                Estoque.unidade_id == pedido.unidade_id,
                Estoque.produto_id == item.produto_id
            )
            .first()
        )

        if not estoque or estoque.quantidade < item.quantidade:
            raise ValueError(f"Estoque insuficiente para o produto {produto.nome}.")

        subtotal = produto.preco * item.quantidade
        valor_total += subtotal

        itens_processados.append({
            "produto": produto,
            "estoque": estoque,
            "quantidade": item.quantidade,
            "preco_unitario": produto.preco
        })

    novo_pedido = Pedido(
        cliente_id=usuario_logado.id,
        unidade_id=pedido.unidade_id,
        canal_pedido=pedido.canal_pedido,
        valor_total=valor_total,
    )

    db.add(novo_pedido)
    db.flush()

    for item in itens_processados:
        item_pedido = ItemPedido(
            pedido_id=novo_pedido.id,
            produto_id=item["produto"].id,
            quantidade=item["quantidade"],
            preco_unitario=item["preco_unitario"],
        )

        item["estoque"].quantidade -= item["quantidade"]
        db.add(item_pedido)

    db.commit()
    db.refresh(novo_pedido)

    return novo_pedido


def consultar_pedido_por_id(db: Session, pedido_id: int) -> Pedido | None:
    return db.query(Pedido).filter(Pedido.id == pedido_id).first()