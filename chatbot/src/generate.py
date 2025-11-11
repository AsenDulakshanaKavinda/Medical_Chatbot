


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
        self.index_name = "test-midical-chatbot"



    def genetate(self, use_input: str):
        try:
            response = self._setup_chain().invoke({"input": use_input})
            return response
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

    def _setup_chain(self, index_name: str = "test-midical-chatbot"):
        try:
            chain = (
                RunnableParallel(
                    context = lambda x: self.retriever.retriever(self.index_name).invoke(x["input"]),
                    input = RunnablePassthrough()
                )
                | self._setup_prompt()
                | self.model_loader.load_llm()
                | RunnableLambda(lambda msg: {"answer": msg.content})
            )
            return chain


        except Exception as e:
            log.error(f"Error while setting-up prompt")
            raise ProjectException(f"Error while seting-up prompt: {str(e)}", sys)







