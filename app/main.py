from fastapi import FastAPI

from app.controllers.user import router

app = FastAPI()

app.include_router(router)
