import smtplib
from email.message import EmailMessage
from src.config import EMAIL_SMTP_SERVER, EMAIL_PORT, EMAIL_USERNAME, EMAIL_PASSWORD

def send_email_alert(message: str, recipient: str):
    msg = EmailMessage()
    msg.set_content(message)
    msg["Subject"] = "Incident Alert"
    msg["From"] = EMAIL_USERNAME
    msg["To"] = recipient

    try:
        with smtplib.SMTP_SSL(EMAIL_SMTP_SERVER, EMAIL_PORT) as server:
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.send_message(msg)
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
