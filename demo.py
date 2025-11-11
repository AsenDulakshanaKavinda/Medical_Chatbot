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

# from chatbot.src.generate import Generate

""" g = Generate()
r = g.genetate("how to prevent heart-attack?")
print(r["answer"]) """

from chatbot.src.generate import Generate

generator = Generate()
response = generator.genetate()

medical_questions = [
    "What are the common symptoms of diabetes?",
    "How can I lower my blood pressure naturally?",
    "What does it mean if I have chest pain after exercising?",
    "When should I see a doctor for a persistent cough?",
    "What are the side effects of taking ibuprofen daily?",
    "How can I tell if I’m dehydrated?",
    "What are the early warning signs of a stroke?",
    "Is it normal to have headaches every day?",
    "What foods help improve liver health?",
    "How much sleep do adults need for optimal health?"
]

for question in medical_questions:
    print(f"Question: {question}")
    print(f"Answer: {generator.genetate(question)}")

    
