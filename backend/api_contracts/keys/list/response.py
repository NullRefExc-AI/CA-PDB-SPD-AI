import cstruct
import backend.api_contracts.constants as constants


class KeyListResponse(cstruct.MemCStruct):
    """
    Defines a response of request to list an API keys
    """

    __def__ = f"""
    struct {{
        int ECODE;
        char API_KEYS[{constants.API_KEY_SIZE * constants.API_KEYS_PER_USER}];
    }}
    """
