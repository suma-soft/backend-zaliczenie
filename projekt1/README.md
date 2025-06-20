# Projekt 1 – TODO List API

RESTful API do zarządzania zadaniami. CRUD, filtrowanie i sortowanie.

## Uruchomienie

```bash
cd projekt1
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload