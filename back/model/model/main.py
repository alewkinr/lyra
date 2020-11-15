import uvicorn
from fastapi import FastAPI
from model.api.v1 import v1
from model.core.config import settings
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(v1, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    # TODO: fix before release
    uvicorn.run(app, host="0.0.0.0", port=8080)
