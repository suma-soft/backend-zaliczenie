#47857
from fastapi import FastAPI
from .routers import notify

app = FastAPI(title="Projekt 9 – System E-mail")

app.include_router(notify.router)

@app.get("/")
def root():
    return {"message": "System powiadomień e-mail działa!"}
