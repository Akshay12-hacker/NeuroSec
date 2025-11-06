import socket
from fastapi import FastAPI
from neural_core import NeuralCore


app = FastAPI()
core = NeuralCore()

@app.get("/")
def root():
    return {"message": "NeuroSec backend is live"}


@app.get("/scan/{host}")
def scan_host(host: str):
    try:
        ip = socket.gethostbyname(host)
        return {"host": host, "ip": ip, "status": "scanned"}
    except Exception as e:
        return {"host": host, "error": str(e)}
    
@app.get("/ai/{query}")
def ai_query(query: str):
    return {"response": core.analyze_input(query)}
