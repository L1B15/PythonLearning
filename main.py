
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello from Azure!",
        "application": "PythonAzureDemo"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
