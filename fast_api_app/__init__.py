from loguru import logger
from app.config import settings
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.schedule import scheduler
from app.middleware import log_request_middleware

# from fastapi_profiler import PyInstrumentProfilerMiddleware


def create_app():
    app = FastAPI(title="FastAPI", servers=[{"url": "/math-ai2"}])
    __config_cors_middleware(app)
    __config_logging(app)
    __register_api_router(app)
    __init_app(app)

    return app


def __config_logging(app) -> None:
    logger.info("Start fast API... 🚀🚀")


def __register_api_router(app) -> None:
    from fast_api_app.api_v1 import api_router

    app.include_router(api_router, prefix=settings.API_V1_STR)


def __config_cors_middleware(app) -> None:
    # Set all CORS enabled origins
    if settings.BACKEND_CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )


def __init_app(app) -> None:
    # app.add_middleware(PyInstrumentProfilerMiddleware)
    app.middleware("http")(log_request_middleware)

app = create_app()
