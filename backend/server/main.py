from backend.server.db import database
from flask import Flask
from backend.server.endpoints.keys import generate, list, cancel
from backend.server.endpoints.meesages import check
from backend.server.endpoints.users import register


app: Flask = Flask(__name__)
app.register_blueprint(generate.blueprint)
app.register_blueprint(list.blueprint)
app.register_blueprint(cancel.blueprint)
app.register_blueprint(register.blueprint)
app.register_blueprint(check.blueprint)


if __name__ == "__main__":
    database.global_init("data/ca-bdb-spd-ai.db")

    app.run(debug=True, port=80)
