import cstruct
import backend.api_contracts.constants as constants


class KeyListRequest(cstruct.MemCStruct):
    """
    Defines a request data to list an API keys
    """

    __def__ = f"""
    struct {{
        char USER_KEY[{constants.USER_KEY_SIZE}];
    }}
    """
