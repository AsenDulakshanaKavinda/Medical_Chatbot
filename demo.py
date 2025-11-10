from chatbot.utils.api_key_loader import ApiKeyManager
from chatbot.utils.model_loader import ModelLoader

am = ApiKeyManager()
ml = ModelLoader()
ml.load_llm()


