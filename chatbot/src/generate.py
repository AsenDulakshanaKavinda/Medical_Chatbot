


import os
import sys
from pathlib import Path
from typing import Iterable, List
from dotenv import load_dotenv

from pinecone import Pinecone
from pinecone import ServerlessSpec


from langchain_core.documents import Document
from langchain_pinecone import PineconeVectorStore
from langchain_core.runnables import RunnablePassthrough, RunnableParallel, RunnableLambda
from langchain_core.prompts import ChatPromptTemplate

from chatbot.src.retriever import Retriever
from chatbot.prompts.prompt import system_prompt
from chatbot.utils.config_loader import load_config
from chatbot.utils.model_loader import ModelLoader
from chatbot.utils.docs_ops import load_documents

from chatbot.logger import logging as log
from chatbot.exception import ProjectException




class Generate:
    def __init__(self):
        self.system_prompt = system_prompt
        self.retriever = Retriever()
        self.model_loader = ModelLoader()



    def genetate(self):
        try:
            response = self._setup_chain().invoke({"input": "what is heart attack?"})
            print(response)
        except Exception as e:
            log.error(f"Error while genetating response")
            raise ProjectException(f"Error while genetating response: {str(e)}", sys)


    def _setup_prompt(self):
        try:
            prompt = ChatPromptTemplate.from_messages(
                [
                    ("system", self.system_prompt),
                    ("human", "{input}")
                ]
            )
            log.info(f"setting-up prompt done.")
            return prompt
        except Exception as e:
            log.error(f"Error while setting-up prompt")
            raise ProjectException(f"Error while setup prompt: {str(e)}", sys)

    def _setup_chain(self):
        try:
            chain = (
                RunnableParallel(
                    context = lambda x: self.retriever.retriever().invoke(x["input"]),
                    input = RunnablePassthrough()
                )
                | self._setup_prompt()
                | self.model_loader.load_llm()
                | RunnableLambda(lambda msg: {"result": msg.__dir__content})
            )
            return chain


        except Exception as e:
            log.error(f"Error while setting-up prompt")
            raise ProjectException(f"Error while seting-up prompt: {str(e)}", sys)







