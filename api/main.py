from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core import tasks

from app.api_v1.api import api_router

from app.db.base_class import Base
from app.db.session import engine

from app.core.config import settings

def get_application():
    app = FastAPI(
        title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
    )

    Base.metadata.create_all(bind=engine)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_event_handler("startup", tasks.create_start_app_handler(app))
    app.add_event_handler("shutdown", tasks.create_stop_app_handler(app))

    return app

app = get_application()
app.include_router(api_router, prefix=settings.API_V1_STR)