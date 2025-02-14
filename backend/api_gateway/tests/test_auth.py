from backend.api_gateway.core.security import hash_password, verify_password

def test_password_hashing():
    password = "securepassword"
    hashed = hash_password(password)
    assert verify_password(password, hashed)

def test_token_creation():
    data = {"sub": "user@example.com"}
    token = create_access_token(data)
    assert decode_token(token)