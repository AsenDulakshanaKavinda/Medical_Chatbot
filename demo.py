""" from chatbot.utils.api_key_loader import ApiKeyManager
from chatbot.utils.model_loader import ModelLoader

ml = ModelLoader()
ml.load_llm()
 """

""" from chatbot.utils.docs_ops import load_documents
load_documents()
 """




""" from chatbot.pipeline.rag_pipeline import test_index, test_retriever, test_generetor
test_generetor() """


""" from chatbot.utils.config_loader import load_config
lc = load_config()

# print(lc)
print(lc["source_data"])
print(lc["index_name"]["test"]) """

from chatbot.src.generate import Generate

g = Generate()
g.genetate("What is heart attack?")


