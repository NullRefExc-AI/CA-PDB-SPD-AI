import json

from backend.server.endpoints.meesages.config.modelconfig import ModelConfig


def load_config():
    with open("data/config.json") as file:
        data = json.load(file)

        return [ModelConfig(**x) for x in data]
