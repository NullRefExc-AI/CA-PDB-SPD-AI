import cstruct
import backend.api_contracts.constants as constants


class MessageCheckRequest(cstruct.MemCStruct):
    """
    Defines a request to check message for redflag
    """

    __def__ = f"""
    struct {{
        char API_KEY[{constants.API_KEY_SIZE}];
        char MESSAGE[{constants.MESSAGE_SIZE}];
    }}
    """
