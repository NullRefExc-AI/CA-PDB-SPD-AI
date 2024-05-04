import cstruct
import backend.api_contracts.constants as constants


class KeyGenerateResponse(cstruct.MemCStruct):
    """
    Defines a response of request to generate an API key
    """

    __def__ = f"""
    struct {{
        int ECODE;
        char API_KEY[{constants.API_KEY_SIZE}]; 
    }}
    """
