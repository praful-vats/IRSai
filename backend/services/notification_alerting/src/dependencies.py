from backend.services.notification_alerting.src.config import SLACK_WEBHOOK_URL, EMAIL_SMTP_SERVER

def get_slack_webhook_url():
    return SLACK_WEBHOOK_URL

def get_email_server_config():
    return {
        "smtp_server": EMAIL_SMTP_SERVER,
        "port": 465
    }
