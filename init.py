import json
from configuration import Configuration


def get_config(filename):
    with open(filename, encoding="UTF-8") as f:
        config = json.load(f)
    configuration = Configuration(config)
    return configuration
