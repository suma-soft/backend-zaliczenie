# Projekt 9 - # System powiadomień e-mail - DSW47857

**Opis:** API do wysyłania automatycznych powiadomień e-mail po zdarzeniach, z obsługą szablonów i SMTP.

## 🚀 Funkcje
- Wysyłka wiadomości e-mail (SMTP)
- Szablony wiadomości tekstowych
- Wysyłka w tle z BackgroundTasks
- Konfiguracja SMTP z pliku .env

## 🧪 Jak uruchomić
```bash
cd projekt9
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload