# Projekt 2 - # System logowania z JWT - DSW47857

**Opis:** System rejestracji i logowania użytkowników z użyciem JWT do autoryzacji i bezpiecznego dostępu do zasobów.

## Funkcje
- Rejestracja użytkowników z hashowaniem haseł
- Logowanie i generowanie tokenów JWT
- Middleware do weryfikacji JWT
- Zabezpieczony endpoint dostępny tylko z tokenem

## Jak uruchomić
```bash
cd projekt2
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload