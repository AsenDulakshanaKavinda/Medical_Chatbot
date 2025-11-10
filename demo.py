""" from chatbot.utils.api_key_loader import ApiKeyManager
from chatbot.utils.model_loader import ModelLoader

ml = ModelLoader()
ml.load_llm()
 """

from chatbot.utils.docs_ops import load_documents
load_documents()
