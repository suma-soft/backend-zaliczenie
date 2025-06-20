from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from .. import models, schemas, auth, database

router = APIRouter(tags=["users"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Użytkownik już istnieje")

    hashed_pw = auth.hash_password(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Nieprawidłowe dane logowania")

    token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/secure-endpoint")
def secure_endpoint(current_user: models.User = Depends(auth.get_current_user)):
    return {"message": f"Cześć, {current_user.username}! Masz dostęp do chronionego zasobu ✔️"}
