from pydantic import BaseModel

class NotificationRequest(BaseModel):
    message: str
    channel: str  # "email" or "slack"
    recipient: str  # Email address or Slack webhook URL
