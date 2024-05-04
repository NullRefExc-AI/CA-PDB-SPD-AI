from flask import request, Blueprint

from backend.server.db import database
from backend.server.db.models import User, APIKey
from backend.api_contracts.keys.list.request import KeyListRequest
from backend.api_contracts.keys.list.response import KeyListResponse

blueprint = Blueprint('keys_list', __name__)


@blueprint.route("/keys/list", methods=["POST"])
def list_api_keys():
    request_data = KeyListRequest()
    request_data.unpack(request.data)

    session = database.create_session()

    user_key = request_data.USER_KEY.decode()
    user = session.query(User).filter_by(user_key=user_key).first()

    if not user:
        response_data = KeyListResponse(ECODE=1).pack()

        return response_data, 403, {'Content-Type': 'application/octet-stream'}

    api_key_structs = "".join([key.api_key for key in session.query(APIKey).filter_by(user_id=user.id).all()])


    response_data = KeyListResponse(ECODE=0, API_KEYS=api_key_structs.encode())
    response_data = response_data.pack()

    return response_data, 200, {'Content-Type': 'application/octet-stream'}