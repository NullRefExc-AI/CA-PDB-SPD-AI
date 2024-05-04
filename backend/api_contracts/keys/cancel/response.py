import cstruct


class KeyCancelResponse(cstruct.MemCStruct):
    """
    Defines a response of request to cancel an API key
    """

    __def__ = """
    struct {
        int ECODE;
    }
    """
