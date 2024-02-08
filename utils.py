import os


def get_api_key():
    return os.getenv('GOOGLE_API_KEY')


api_key = get_api_key()
print(api_key)
