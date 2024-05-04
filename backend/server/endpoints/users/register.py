from flask import Blueprint

from backend.server.db import database
from backend.server.db.models import User
from backend.api_contracts.users.register.request import UserRegisterRequest
from backend.api_contracts.users.register.response import UserRegisterResponse
from random import choice
from string import ascii_letters

blueprint = Blueprint('user_register', __name__)


@blueprint.route("/user/register", methods=["POST"])
def register_user():
    new_user_key = "".join([choice(ascii_letters) for _ in range(8192)])

    session = database.create_session()

    new_user = User(user_key=new_user_key)
    session.add(new_user)
    session.commit()

    response_data = UserRegisterResponse(ECODE=0, USER_KEY=new_user_key.encode()).pack()
    return response_data, 200, {'Content-Type': 'application/octet-stream'}