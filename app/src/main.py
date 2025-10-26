from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return{
        "service": os.getenv("SERVICE_NAME","microservice"),
        "env": os.getenv("ENV", "dev"),
        "message": "OK Prueba 4"
    }