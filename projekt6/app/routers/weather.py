from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, weather

router = APIRouter(tags=["Weather"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/weather")
async def get_weather(city: str, db: Session = Depends(get_db)):
    result = await weather.fetch_weather(city)
    if not result:
        raise HTTPException(status_code=404, detail="Nie znaleziono miasta")

    # Zapisz zapytanie do bazy
    record = models.WeatherQuery(
        city=result["city"],
        temperature=f"{result['temperature']} °C",
        condition=result["condition"]
    )
    db.add(record)
    db.commit()
    db.refresh(record)

    return {
        "city": result["city"],
        "temperature": result["temperature"],
        "condition": result["condition"]
    }
