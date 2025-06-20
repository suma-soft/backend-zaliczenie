from fastapi import FastAPI
from .database import Base, engine
from .routers import users

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Projekt 2 – JWT Auth")

app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "System logowania JWT działa! 🔐"}
