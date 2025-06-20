from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel, EmailStr
from ..email_utils import send_email

router = APIRouter(tags=["Notification"])

class EmailRequest(BaseModel):
    email: EmailStr
    username: str

@router.post("/send-email")
def send_welcome_email(data: EmailRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(
        send_email,
        to=data.email,
        subject="Witamy w systemie!",
        template_file="welcome.txt",
        context={"username": data.username}
    )
    return {"message": f"Email do {data.email} zostanie wysłany w tle."}
