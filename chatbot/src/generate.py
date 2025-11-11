
import os
import sys

from langchain_core.runnables import RunnablePassthrough, RunnableParallel, RunnableLambda
from langchain_core.prompts import ChatPromptTemplate

from chatbot.src.retriever import Retriever
from chatbot.prompts.prompt import system_prompt
from chatbot.utils.config_loader import load_config
from chatbot.utils.model_loader import ModelLoader


from chatbot.logger import logging as log
from chatbot.exception import ProjectException




class Generate:
    def __init__(self):
        self.system_prompt = system_prompt
        self.retriever = Retriever()
        self.model_loader = ModelLoader()
        self.config = load_config()

        if os.getenv("ENV", "local").lower() != "production":
            self.index_name = load_config()["index_name"]["dev"]
            log.info("Running in LOCAL INDEX: env loaded.")
        else:
            self.index_name = load_config()["index_name"]["production"]
            log.info("Running in PRODUCTION INDEX!!!")

    def genetate(self, use_input: str):
        try:
            payload = {"input": use_input}
            response = self._setup_chain().invoke(payload)
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

    def _setup_chain(self):
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







