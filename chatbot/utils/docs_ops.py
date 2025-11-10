import sys
from pathlib import Path
from typing import Iterable, List


from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

from chatbot.utils.config_loader import load_config

from chatbot.logger import logging as log
from chatbot.exception import ProjectException



def load_documents() -> List[Document]:
    log.info("Loading documents started")
    config = load_config()
    source_data = config["source_data"]
    try:
        loader = DirectoryLoader(
            path=source_data,
            glob="*.pdf",
            loader_cls=PyPDFLoader
        )
        documents = loader.load()
        log.info(f"{len(documents)} documents loaded")
        return documents
    except Exception as e:
        log.error(f"Error while loading documents")
        raise ProjectException(f"Error while loading documents: {str(e)}", sys)










