import cstruct
import backend.api_contracts.constants as constants


class UserRegisterResponse(cstruct.MemCStruct):
    """
    Defines a response to request to register a user
    """

    __def__ = f"""
    struct {{
        int ECODE;
        char USER_KEY[{constants.USER_KEY_SIZE}];
    }}
    """
