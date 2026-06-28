from pydantic import BaseModel, ConfigDict


class ProdutoCreate(BaseModel):
    nome: str
    descricao: str | None = None
    preco: float
    categoria: str
    ativo: bool = True


class ProdutoResponse(BaseModel):
    id: int
    nome: str
    descricao: str | None
    preco: float
    categoria: str
    ativo: bool

    model_config = ConfigDict(from_attributes=True)