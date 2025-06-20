from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class WeatherQuery(Base):
    __tablename__ = "weather_queries"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    temperature = Column(String)
    condition = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
