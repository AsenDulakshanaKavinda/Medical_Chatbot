import sys

from langchain_pinecone import PineconeVectorStore

from chatbot.utils.model_loader import ModelLoader

from chatbot.logger import logging as log
from chatbot.exception import ProjectException

class Retriever:
    def __init__(self):
        self.model_loader = ModelLoader()

    def retriever(self, index_name: str):
        try:
            index_search = PineconeVectorStore.from_existing_index(
                index_name=index_name,
                embedding=self.model_loader.load_embedding()
            )
            log.info(f"Retriever created!!!")
            return index_search.as_retriever(search_type="similarity", search_kwargs={"k": 3})
        except Exception as e:
            log.error(f"Error while creating retriever")
            raise ProjectException(f"Error while creating retriever: {str(e)}", sys)











