
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

load_dotenv()


class ChatIngestor:
    def __init__(self):
        self.model_loader = ModelLoader()
        self.documents = load_documents()

    def indexing(self, index_name: str):
        
        try:
            PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
            pinecone_api_key = PINECONE_API_KEY
            pc = Pinecone(api_key=pinecone_api_key)

            if not pc.has_index(index_name):
                self._create_index(pc=pc, index_name=index_name)


            index_to = PineconeVectorStore.from_documents(
                documents = self._filter_to_minimal_docs(self.documents),
                embedding = self.model_loader.load_embedding(),
                index_name = index_name
            )
            log.info(f"Indexing is complited....")

        except Exception as e:
            log.error(f"Error while indexing")
            raise ProjectException(f"Error while indexing: {str(e)}", sys)


        
    def _create_index(self, pc, index_name: str):
        try:
            pc.create_index(
                    name=index_name,
                    dimension=384,
                    metric="cosine",
                    spec=ServerlessSpec(cloud="aws", region="us-east-1")
            )
            index = pc.Index(index_name)
            log.info(f"Pinecone index: {index_name} is creates...")

        except Exception as e:
            log.error(f"Error while creating Index")
            raise ProjectException(f"Error while creating Index: {str(e)}", sys)



    def _doc_splitter(self, min_docs: List[Document], chunk_size=500, chunk_overlap=200) -> List[Document]:
        try:
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap
            )
            chunks = splitter.split_documents(min_docs)
            log.info(f"{len(chunks)} minimal documents are created")
            return chunks
        except Exception as e:
            log.error(f"Error while creating chunks")
            raise ProjectException(f"Error while creating chunks: {str(e)}", sys)

        

    def _filter_to_minimal_docs(self, docs: List[Document]) -> List[Document]:
        """
        Given a list of Document objects, return a new list of Document objects
        containing only 'source' in metadata and the original page_content.
        """

        try:
            log.info("Creating minimal documents starded")
            minimal_docs: List[Document] = []
            for doc in docs:
                src = doc.metadata.get("source")
                minimal_docs.append(
                    Document(
                        page_content=doc.page_content,
                        metadata={"source": src}
                    )
                )
            log.info(f"{len(minimal_docs)} minimal documents are created")
            return minimal_docs
        except Exception as e:
            log.error(f"Error while creating minimal documents")
            raise ProjectException(f"Error while creating minimal documents: {str(e)}", sys)








