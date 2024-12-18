from fastapi import FastAPI

from formvalidator.database import init_db
from formvalidator.routers.form_router import router

app = FastAPI()

init_db()

app.include_router(router)
