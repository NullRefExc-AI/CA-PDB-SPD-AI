from flask import request, Blueprint

from backend.server.db import database
from backend.server.db.models import User, APIKey
from backend.api_contracts.keys.generate.request import KeyGenerateRequest
from backend.api_contracts.keys.generate.response import KeyGenerateResponse
from random import choice
from string import ascii_letters

blueprint = Blueprint('keys_generate', __name__)


@blueprint.route("/keys/generate", methods=["POST"])
def generate_api_key():
    request_data = KeyGenerateRequest()
    request_data.unpack(request.data)

    user_key = request_data.USER_KEY.decode()

    session = database.create_session()
    user = session.query(User).filter_by(user_key=user_key).first()

    if not user:
        response_data = KeyGenerateResponse(ECODE=1).pack()
        return response_data, 403, {'Content-Type': 'application/octet-stream'}

    new_api_key_str = "".join([choice(ascii_letters) for _ in range(16384)])

    new_api_key = APIKey(api_key=new_api_key_str, user_id=user.id)

    session.add(new_api_key)
    session.commit()

    response_data = KeyGenerateResponse(ECODE=0, API_KEY=new_api_key_str.encode()).pack()
    return response_data, 200, {'Content-Type': 'application/octet-stream'}