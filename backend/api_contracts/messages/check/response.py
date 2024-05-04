import cstruct
import backend.api_contracts.constants as constants


class Redflag(cstruct.MemCStruct):
    """
    Defines an info about redflag detection in message
    """

    __def__ = f"""
    struct {{
        char CODENAME[{constants.REDFLAG_CODENAME_LENGTH}];
        char DESCRIPTION[{constants.REDFLAG_DESCRIPTION_LENGTH}];
        float NEUTRAL_WEIGHT;
        float REDFLAG_WEIGHT;
    }}
    """


class MessageCheckResponse(cstruct.MemCStruct):
    __byte_order__ = cstruct.NATIVE_ORDER
    """
    Defines a response to request to check message for redflags
    """

    __def__ = f"""
    typedef struct Redflag Redflag;
    
    struct {{
        int ECODE;
        char RED_FLAGS[{constants.MAX_MODELS_COUNT * Redflag().size}];
    }}
    """
