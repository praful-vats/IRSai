import requests

def send_slack_alert(message: str, webhook_url: str):
    payload = {"text": message}
    response = requests.post(webhook_url, json=payload)
    return {"status": "success" if response.status_code == 200 else "error"}
