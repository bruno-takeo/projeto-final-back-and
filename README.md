# Projeto Final - Análise e Desenvolvimento de Sistemas

## Sistema de Gestão da Rede de Restaurantes "Raízes do Nordeste"

### Descrição

Este projeto foi desenvolvido como requisito para conclusão do curso de Análise e Desenvolvimento de Sistemas da UNINTER.

A aplicação consiste em uma API REST desenvolvida em Python utilizando o framework FastAPI para gerenciamento de uma rede fictícia de restaurantes denominada **Raízes do Nordeste**. O sistema contempla funcionalidades de autenticação de usuários, gerenciamento de produtos, unidades, controle de estoque, realização de pedidos e processamento de pagamentos simulados (Mock Payment).

O projeto foi desenvolvido seguindo uma arquitetura em camadas, separando responsabilidades entre modelos, serviços, rotas, esquemas de validação e mecanismos de segurança.

---

## Tecnologias Utilizadas

* Python 3.12
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn
* JWT (python-jose)
* Passlib (bcrypt)
* Git
* GitHub
* Draw.io

---

## Funcionalidades Implementadas

* Cadastro de usuários
* Autenticação utilizando JWT
* Proteção de rotas por perfil de usuário
* Cadastro de produtos
* Cadastro de unidades
* Controle de estoque
* Criação de pedidos
* Validação automática de estoque
* Atualização do estoque após a venda
* Pagamento Mock
* Atualização automática do status do pedido
* Documentação automática da API utilizando Swagger

---

## Estrutura do Projeto

```
app/
│
├── api
├── db
├── models
├── schemas
├── security
├── services
└── main.py
```

---

## Execução do Projeto

Criar ambiente virtual:

```bash
python -m venv .venv
```

Ativar ambiente virtual:

```bash
source .venv/Scripts/activate
```

Instalar dependências:

```bash
pip install -r requirements.txt
```

Executar a aplicação:

```bash
uvicorn app.main:app --reload
```

Documentação da API:

```
http://localhost:8000/docs
```

---

## Fluxo Sugerido de Teste

Após iniciar a aplicação, acesse o Swagger em:

http://localhost:8000/docs

### 1. Criar usuário administrador

Endpoint:

POST /usuarios/

Body:

{
  "nome": "Admin Teste",
  "email": "admin@email.com",
  "senha": "123456",
  "perfil": "ADMIN",
  "consentimento_lgpd": true
}

### 2. Fazer login

Endpoint:

POST /auth/login

Body:

{
  "email": "admin@email.com",
  "senha": "123456"
}

Copie o campo `access_token` retornado.

### 3. Autorizar no Swagger

Clique em **Authorize** no topo da página do Swagger e informe:

Bearer SEU_TOKEN_AQUI

### 4. Criar produto

POST /produtos/

{
  "nome": "Tapioca de queijo coalho",
  "descricao": "Tapioca recheada com queijo coalho",
  "preco": 12.9,
  "categoria": "Tapiocas",
  "ativo": true
}

### 5. Criar unidade

POST /unidades/

{
  "nome": "Raízes do Nordeste - Recife Centro",
  "cidade": "Recife",
  "estado": "PE",
  "ativa": true
}

### 6. Criar estoque

POST /estoques/

{
  "unidade_id": 1,
  "produto_id": 1,
  "quantidade": 20
}

### 7. Criar pedido

POST /pedidos/

{
  "unidade_id": 1,
  "canal_pedido": "APP",
  "itens": [
    {
      "produto_id": 1,
      "quantidade": 2
    }
  ]
}

### 8. Processar pagamento mock

POST /pagamentos/1

{
  "aprovado": true
}

### 9. Consultar pedido

GET /pedidos/1

O pedido deverá retornar com status `PAGO`.

## Autor

Bruno Takeo Barbosa Kaahara
Curso de Análise e Desenvolvimento de Sistemas – UNINTER

