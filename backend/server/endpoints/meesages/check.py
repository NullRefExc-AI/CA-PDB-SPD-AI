import numpy as np
from flask import Blueprint, request

from ai.abstract.load.model import Model
from backend.server.db import database
from backend.server.db.models import User, APIKey
from backend.api_contracts.messages.check.request import MessageCheckRequest
from backend.api_contracts.messages.check.response import MessageCheckResponse, Redflag
from backend.server.endpoints.meesages.config.load import load_config
from threading import Lock

from backend.server.endpoints.meesages.config.modelconfig import ModelConfig

models_mutex = Lock()
# Commented because can't load models on windows
# models = [Model(model) for model in load_config()]

blueprint = Blueprint('message_check', __name__)


@blueprint.route("/messages/check", methods=["POST"])
def register_user():
    request_data = MessageCheckRequest()
    request_data.unpack(request.data)

    session = database.create_session()

    api_key = request_data.API_KEY.decode()
    key = session.query(APIKey).filter_by(api_key=api_key).first()

    if not key:
        response_data = MessageCheckResponse(ECODE=1).pack()

        return response_data, 403, {'Content-Type': 'application/octet-stream'}

    redflags = bytes()

    with models_mutex:
        for model_config in [
            ModelConfig("PIE", "likes going to windows or playing with knifes", "STUB"),
            ModelConfig("DARKNESS", "very egoistic people with psychopathy (no complex feelings such as love)", "STUB"),
        ]:
            redflags += Redflag(
                CODENAME=model_config.codename.encode(),
                DESCRIPTION=model_config.description.encode(),
                NEUTRAL_WEIGHT=0.1,
                REDFLAG_WEIGHT=0.9
            ).pack()

    response_data = MessageCheckResponse(ECODE=0, RED_FLAGS=redflags).pack()
    return response_data, 200, {'Content-Type': 'application/octet-stream'}