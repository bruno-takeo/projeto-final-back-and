import enum


class PerfilUsuario(str, enum.Enum):
    CLIENTE = "CLIENTE"
    ATENDENTE = "ATENDENTE"
    GERENTE = "GERENTE"
    ADMIN = "ADMIN"