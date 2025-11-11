
from chatbot.utils.config_loader import load_config


config = load_config()
print(config["index_name"]["test"])
print(type(config["index_name"]["test"]))

print(load_config()["index_name"]["test"])
