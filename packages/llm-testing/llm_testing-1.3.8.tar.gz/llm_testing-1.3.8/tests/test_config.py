import os
import pytest
from gemini.config import set_google_api_key, get_google_api_key

def test_set_google_api_key():

    test_api_key = "test-key-123"
    set_google_api_key(test_api_key)
    assert os.environ["GOOGLE_API_KEY"] == test_api_key

def test_get_google_api_key():

    test_api_key = "test-key-123"
    os.environ["GOOGLE_API_KEY"] = test_api_key
    assert get_google_api_key() == test_api_key

def test_get_google_api_key_not_set():

    if "GOOGLE_API_KEY" in os.environ:
        del os.environ["GOOGLE_API_KEY"]
    with pytest.raises(ValueError, match="GOOGLE_API_KEY environment variable not set. Use `set_google_api_key` to configure it."):
        get_google_api_key()
