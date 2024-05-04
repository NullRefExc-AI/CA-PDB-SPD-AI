import cstruct
import requests
from cstruct import MemCStruct

from backend.api_contracts.messages.check.request import MessageCheckRequest
from backend.api_contracts.messages.check.response import MessageCheckResponse, Redflag


def main():
    # Prompt for API key and message
    api_key = input("Enter your API key: ").encode()
    message = input("Enter the message to check: ")

    # Create request data
    request_data = MessageCheckRequest()
    request_data.API_KEY = api_key
    request_data.MESSAGE = message.encode('utf-16le')  # Encode as UTF-16 little-endian

    # Send request
    url = "http://localhost/messages/check"  # Replace with your server address
    response = requests.post(url, data=request_data.pack(), headers={'Content-Type': 'application/octet-stream'})

    # Parse response
    response_data = MessageCheckResponse()
    response_data.unpack(response.content)

    # Print response
    if response_data.ECODE == 0:
        print("Red flag analysis results:")
        for i in range(0, len(response_data.RED_FLAGS), Redflag().size):
            redflag_bytes = response_data.RED_FLAGS[i:Redflag().size]
            redflag = Redflag()
            redflag.unpack(redflag_bytes)
            if redflag_bytes:  # Check if codename is not empty
                codename = redflag.CODENAME.decode().strip('\x00')
                description = redflag.DESCRIPTION.decode().strip('\x00')
                neutral_weight = redflag.NEUTRAL_WEIGHT
                redflag_weight = redflag.REDFLAG_WEIGHT
                print(f" - Codename: {codename}")
                print(f"   Description: {description}")
                print(f"   Neutral weight: {neutral_weight:.4f}")
                print(f"   Red flag weight: {redflag_weight:.4f}")
    elif response_data.ECODE == 1:
        print("Error: Invalid API key.")
    else:
        print("Unknown error.")


if __name__ == "__main__":
    main()