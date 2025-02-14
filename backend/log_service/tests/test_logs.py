from backend.api.utils.redis_clients import set_cache, get_cache

def test_redis_cache():
    set_cache("test_key", "test_value", 10)
    assert get_cache("test_key").decode("utf-8") == "test_value"
