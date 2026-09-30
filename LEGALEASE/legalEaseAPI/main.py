from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from legalEaseAPI.routes import router

app = FastAPI(
    title="LegalEase API",
    description="AI-Powered Legal Document Generator",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/api-info")
def api_info():
    return {
        "application": "LegalEase",
        "description": "AI-Powered Legal Document Generator",
        "backend": "FastAPI",
        "status": "running",
    }
