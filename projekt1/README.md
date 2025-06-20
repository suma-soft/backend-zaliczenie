# Projekt 1 – # TODO API - DSW47857

**Opis:** RESTful API do zarządzania zadaniami z pełną obsługą CRUD, filtrowaniem oraz sortowaniem.

## Funkcje
- CRUD dla zadań (Create, Read, Update, Delete)
- Filtrowanie po statusie i priorytecie
- Sortowanie po dacie utworzenia
- Użycie FastAPI + SQLite (SQLAlchemy)

## Jak uruchomić
```bash
cd projekt1
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload