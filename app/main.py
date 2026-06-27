from fastapi import FastAPI
from app.db.database import Base, engine

app = FastAPI(
    title="API Raízes do Nordeste",
    description="API Back-end para gestão de pedidos, estoque, fidelização e pagamento mock da rede Raízes do Nordeste.",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {
        "message": "Bem-vindo à API Raízes do Nordeste",
        "status": "online"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "API Raízes do Nordeste"
    }