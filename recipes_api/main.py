import uvicorn
from contextlib import asynccontextmanager
from core.models import Base, db_helper
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from api_v1 import router as router_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router_v1, prefix=settings.api_v1_prefix)
app.add_middleware(CORSMiddleware, 
                   allow_origins=settings.origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],)


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)