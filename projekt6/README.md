# Projekt 6 - # API pogodowe - DSW47857

**Opis:** API do pobierania prognozy pogody z OpenWeatherMap oraz zapisywania historii zapytań.

## Funkcje
- Integracja z OpenWeatherMap API
- Endpoint do pobierania prognozy dla miasta
- Zapis zapytań pogodowych w bazie SQLite
- Wczytywanie API key z .env

## Jak uruchomić
```bash
cd projekt6
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload