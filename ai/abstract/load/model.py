import tensorflow as tf
from backend.server.endpoints.meesages.config.modelconfig import ModelConfig


class Model:
    BUFFER_SIZE = 10000
    BATCH_SIZE = 64

    model: tf.keras.Model

    codename: str
    description: str

    def __init__(self, model_config: ModelConfig):
        model = tf.keras.models.load_model(model_config.weights_path)

        self.codename = model_config.codename
        self.description = model_config.description
