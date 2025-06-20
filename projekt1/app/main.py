#47857
from fastapi import FastAPI
from .routers import tasks
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="TODO API")

app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "TODO API działa! ✔️"}
