import cstruct
import requests
import backend.api_contracts.constants as constants
from backend.api_contracts.keys.list.request import KeyListRequest
from backend.api_contracts.keys.list.response import KeyListResponse


def main():
    # Prompt for user key
    user_key = input("Enter your user key: ").encode()

    # Create request data
    request_data = KeyListRequest()
    request_data.USER_KEY = user_key

    # Send request
    url = "http://localhost/keys/list"  # Replace with your server address
    response = requests.post(url, data=request_data.pack(), headers={'Content-Type': 'application/octet-stream'})

    # Parse response
    response_data = KeyListResponse()
    response_data.unpack(response.content)

    # Print response
    if response_data.ECODE == 0:
        print("API keys for your user:")
        for i in range(0, len(response_data.API_KEYS), 16384):
            decoded_key = response_data.API_KEYS[i:i+16384].decode()
            if decoded_key[0] != "\0":
                print(decoded_key)
    elif response_data.ECODE == 1:
        print("Error: Invalid user key.")
    else:
        print("Unknown error.")


if __name__ == "__main__":
    main()