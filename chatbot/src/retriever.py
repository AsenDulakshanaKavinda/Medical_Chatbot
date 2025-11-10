import os
import sys
from pathlib import Path
from typing import Iterable, List
from dotenv import load_dotenv

from pinecone import Pinecone
from pinecone import ServerlessSpec


from langchain_core.documents import Document
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter

from chatbot.utils.config_loader import load_config
from chatbot.utils.model_loader import ModelLoader
from chatbot.utils.docs_ops import load_documents

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











