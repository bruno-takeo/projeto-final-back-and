import enum


class PerfilUsuario(str, enum.Enum):
    CLIENTE = "CLIENTE"
    ATENDENTE = "ATENDENTE"
    GERENTE = "GERENTE"
    ADMIN = "ADMIN"


class CanalPedido(str, enum.Enum):
    APP = "APP"
    WEB = "WEB"
    BALCAO = "BALCAO"
    TOTEM = "TOTEM"
    PICKUP = "PICKUP"


class StatusPedido(str, enum.Enum):
    AGUARDANDO_PAGAMENTO = "AGUARDANDO_PAGAMENTO"
    PAGO = "PAGO"
    EM_PREPARO = "EM_PREPARO"
    PRONTO = "PRONTO"
    ENTREGUE = "ENTREGUE"
    CANCELADO = "CANCELADO"


class FormaPagamento(str, enum.Enum):
    MOCK = "MOCK"


class StatusPagamento(str, enum.Enum):
    PENDENTE = "PENDENTE"
    APROVADO = "APROVADO"
    RECUSADO = "RECUSADO"