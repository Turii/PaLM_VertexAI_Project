import os
import google.generativeai as palm
from google.api_core import client_options as client_options_lib

from utils import get_api_key


api_key = get_api_key()
print(api_key)


palm.configure(
    api_key=get_api_key(),
    transport="rest",
    client_options=client_options_lib.ClientOptions(
        api_endpoint=os.getenv("GOOGLE_API_BASE"),
    )
)

