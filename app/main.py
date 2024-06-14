from fastapi import FastAPI
from app.api import books
from app.core import database

app = FastAPI()

app.include_router(books.router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.shutdown()
