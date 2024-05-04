import cstruct
import backend.api_contracts.constants as constants


class KeyGenerateRequest(cstruct.MemCStruct):
    """
    Defines a request data to generate a API key
    """

    __def__ = f"""
    struct {{
        char USER_KEY[{constants.USER_KEY_SIZE}];
    }}
    """
