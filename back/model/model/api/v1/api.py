from fastapi import APIRouter
from model.api.v1 import v1_sessions

v1 = APIRouter()
v1.include_router(v1_sessions.router, prefix="/sessions", tags=["v1_sessions"])
