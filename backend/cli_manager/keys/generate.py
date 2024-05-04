import cstruct
import requests
import backend.api_contracts.constants as constants
from backend.api_contracts.keys.generate.request import KeyGenerateRequest
from backend.api_contracts.keys.generate.response import KeyGenerateResponse


def main():
    # Prompt for user key
    user_key = input("Enter your user key: ").encode()

    # Create request data
    request_data = KeyGenerateRequest()
    request_data.USER_KEY = user_key

    # Send request
    url = "http://localhost/keys/generate"  # Replace with your server address
    response = requests.post(url, data=request_data.pack(), headers={'Content-Type': 'application/octet-stream'})

    # Parse response
    response_data = KeyGenerateResponse()
    response_data.unpack(response.content)

    # Print response
    if response_data.ECODE == 0:
        print("API key successfully generated:")
        print(response_data.API_KEY.decode())
    elif response_data.ECODE == 1:
        print("Error: Invalid user key.")
    else:
        print("Unknown error.")


if __name__ == "__main__":
    main()