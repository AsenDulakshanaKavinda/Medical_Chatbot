""" from chatbot.utils.api_key_loader import ApiKeyManager
from chatbot.utils.model_loader import ModelLoader

ml = ModelLoader()
ml.load_llm()
 """

""" from chatbot.utils.docs_ops import load_documents
load_documents()
 """




from chatbot.pipeline.rag_pipeline import test_index, test_retriever, test_generetor
test_generetor()
