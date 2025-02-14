import requests

def http_client(url: str, method: str = "GET", data: dict = None):
    try:
        response = requests.request(method, url, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}