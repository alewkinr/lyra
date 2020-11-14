from fastapi import APIRouter
from model.api.v1 import v1_models

v1 = APIRouter()
v1.include_router(v1_models.router, prefix="/models", tags=["v1_models"])
