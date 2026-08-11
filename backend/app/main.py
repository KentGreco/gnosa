from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel

class HealthResponse(BaseModel):
    status: Literal["ok"]
    service: Literal["gnosa-backend"]

app = FastAPI(
    title="Gnosa Backend"
    version="0.1.0"
)

@app.get("/health", response_model=HealthResponse)
def get_health() -> HealthResponse:
    return HealthResponse(
        status="ok",
        service="gnosa-backend",
    )
