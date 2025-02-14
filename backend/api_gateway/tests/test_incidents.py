from backend.api_gateway.routes.incidents import get_incidents

def test_get_incidents():
    response = get_incidents()
    assert "incidents" in response
