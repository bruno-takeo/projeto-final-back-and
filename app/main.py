from fastapi import FastAPI

app = FastAPI(
    title="API Raízes do Nordeste",
    description="API Back-end para gestão de pedidos, estoque, fidelização e pagamento mock da rede Raízes do Nordeste.",
    version="1.0.0"
)


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