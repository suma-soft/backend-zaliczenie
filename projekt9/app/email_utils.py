import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template
from dotenv import load_dotenv
import os

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

TEMPLATES_DIR = Path(__file__).parent / "templates"

def render_template(filename: str, context: dict) -> str:
    with open(TEMPLATES_DIR / filename, "r", encoding="utf-8") as file:
        template = Template(file.read())
    return template.safe_substitute(**context)

def send_email(to: str, subject: str, template_file: str, context: dict):
    body = render_template(template_file, context)

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = SMTP_USERNAME
    msg["To"] = to
    msg.set_content(body)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.send_message(msg)
