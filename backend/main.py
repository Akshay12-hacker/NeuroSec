import socket
from fastapi import FastAPI
from neural_core import NeuralCore
from sentinel import system_status
from recon import get_ip_info
from intel_core import rank_risk

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

@app.get("/status")
def status():
    return system_status()

@app.get("/ai/status")
def ai_status():
    data = system_status()
    msg = f"CPU Usage: {data['cpu_usage']}, Memory Usage: {data['memory_usage']}, System Boot Time: {data['system_boot_time']}"
    return{"analysis": core.analyze_input("status"), "system_info": msg}

@app.get("/ip/{ip}")
def ip_info(ip: str):
    return get_ip_info(ip)

@app.get("/ip-risk/{ip}")
def risk_lookup(ip: str):
    info = get_ip_info(ip)
    if "error" in info:
        return {"ip": ip, "error": info["error"]}
    
    risk = rank_risk(info)
    return{
        "ip": ip,
        "risk_level": risk,
        "details": info
    }