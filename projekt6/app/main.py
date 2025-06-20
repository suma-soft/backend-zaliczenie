from fastapi import FastAPI
from .database import Base, engine
from .routers import weather

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Projekt 6 – API Pogodowe")

app.include_router(weather.router)

@app.get("/")
def root():
    return {"message": "API pogodowe działa ☀️"}
