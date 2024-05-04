import cstruct
import requests
from backend.api_contracts.users.register.request import UserRegisterRequest
from backend.api_contracts.users.register.response import UserRegisterResponse


def main():
    # Send request
    url = "http://127.0.0.1/user/register"  # Replace with your server address
    response = requests.post(url)

    # Parse response
    response_data = UserRegisterResponse()
    response_data.unpack(response.content)

    # Print response
    if response_data.ECODE == 0:
        print("User successfully registered!")
        print("Your user key is:", response_data.USER_KEY.decode())
    else:
        print("Error during registration.")


if __name__ == "__main__":
    main()