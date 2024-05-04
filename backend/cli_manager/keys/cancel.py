import cstruct
import requests
import backend.api_contracts.constants as constants
from backend.api_contracts.keys.cancel.request import KeyCancelRequest
from backend.api_contracts.keys.cancel.response import KeyCancelResponse


def main():
    # Prompt for user and API key
    user_key = input("Enter your user key: ").encode()
    api_key = input("Enter the API key to cancel: ").encode()

    # Create request data
    request_data = KeyCancelRequest()
    request_data.USER_KEY = user_key
    request_data.API_KEY = api_key

    # Send request
    url = "http://localhost/keys/cancel"  # Replace with your server address
    response = requests.post(url, data=request_data.pack(), headers={'Content-Type': 'application/octet-stream'})

    # Parse response
    response_data = KeyCancelResponse()
    response_data.unpack(response.content)

    # Print response
    if response_data.ECODE == 0:
        print("API key successfully cancelled.")
    elif response_data.ECODE == 1:
        print("Error: Invalid user key.")
    elif response_data.ECODE == 2:
        print("Error: Invalid API key.")
    else:
        print("Unknown error.")


if __name__ == "__main__":
    main()