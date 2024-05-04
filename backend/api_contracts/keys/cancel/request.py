import cstruct
import backend.api_contracts.constants as constants


class KeyCancelRequest(cstruct.MemCStruct):
    """
    Defines a request data to cancel a API key
    """

    __def__ = f"""
    struct {{
        char USER_KEY[{constants.USER_KEY_SIZE}];
        char API_KEY[{constants.API_KEY_SIZE}];
    }}
    """
