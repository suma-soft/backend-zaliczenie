# Backend Zalicznie – Projekty FastAPI - DSW47857

Repozytorium zawiera zestaw projektów wykonanych w ramach zaliczenia przedmiotu z programowania backendowego. Każdy projekt znajduje się w osobnym katalogu i został zbudowany przy użyciu **FastAPI**, **SQLAlchemy**, **SQLite**, oraz innych nowoczesnych narzędzi backendowych.

---

## 📁 Projekty

### ✅ [Projekt 1 – TODO API](./projekt1)
RESTful API do zarządzania zadaniami z CRUD, filtrowaniem i sortowaniem.

### ✅ [Projekt 2 – System logowania z JWT](./projekt2)
Rejestracja, logowanie i autoryzacja użytkowników z JWT + chronione trasy.

### ✅ [Projekt 6 – API pogodowe](./projekt6)
Integracja z OpenWeatherMap API oraz zapisywanie historii zapytań pogodowych.

### ✅ [Projekt 9 – System powiadomień e-mail](./projekt9)
Wysyłanie e-maili po zdarzeniach z wykorzystaniem SMTP i szablonów.

---

## 🔧 Jak uruchomić projekty?

Każdy projekt ma własny `README.md` z instrukcją uruchomienia, zależnościami i opisem funkcjonalności. Standardowo:

```bash
cd projektX
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload