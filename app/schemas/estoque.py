from pydantic import BaseModel, ConfigDict


class EstoqueCreate(BaseModel):
    unidade_id: int
    produto_id: int
    quantidade: int


class EstoqueResponse(BaseModel):
    id: int
    unidade_id: int
    produto_id: int
    quantidade: int

    model_config = ConfigDict(from_attributes=True)