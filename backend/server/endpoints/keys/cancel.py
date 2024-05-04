from flask import request, Blueprint

from backend.server.db import database
from backend.server.db.models import User, APIKey
from backend.api_contracts.keys.cancel.request import KeyCancelRequest
from backend.api_contracts.keys.cancel.response import KeyCancelResponse

blueprint = Blueprint('keys_cancel', __name__)


@blueprint.route("/keys/cancel", methods=["POST"])
def cancel_api_key():
    request_data = KeyCancelRequest()
    request_data.unpack(request.data)

    session = database.create_session()
    user_key = request_data.USER_KEY.decode()
    api_key_to_cancel = request_data.API_KEY.decode()

    user = session.query(User).filter_by(user_key=user_key).first()

    if not user:
        response_data = KeyCancelResponse(ECODE=1).pack()
        return response_data, 403, {'Content-Type': 'application/octet-stream'}

    api_key = session.query(APIKey).filter_by(user_id=user.id, api_key=api_key_to_cancel).first()

    if not api_key:
        response_data = KeyCancelResponse(ECODE=2).pack()
        return response_data, 400, {'Content-Type': 'application/octet-stream'}

    session.delete(api_key)
    session.commit()

    response_data = KeyCancelResponse(ECODE=0).pack()
    return response_data, 200, {'Content-Type': 'application/octet-stream'}