from dataclasses import dataclass


@dataclass
class ModelConfig:
    codename: str
    description: str
    weights_path: str
