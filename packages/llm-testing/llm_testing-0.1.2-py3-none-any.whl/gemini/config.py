import os

def set_google_api_key(api_key: str):
    os.environ["GOOGLE_API_KEY"] = api_key

def get_google_api_key():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set. Use `set_google_api_key` to configure it.")
    return api_key


def set_openai_api_key(api_key: str):
    os.environ["OPENAI_API_KEY"]=api_key

def get_openai_api_key():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set. Use `set_openai_api_key` to configure it.")
    return api_key

