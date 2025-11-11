import os
import sys

from dotenv import load_dotenv

from chatbot.logger import logging as log
from chatbot.exception import ProjectException

from chatbot.utils.config_loader import load_config
from chatbot.utils.api_key_loader import ApiKeyManager

from langchain_mistralai import ChatMistralAI, MistralAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

class ModelLoader:
    def __init__(self):
        """"
        If the environment is not production, 
        load the .env file and run in local/development mode; 
        otherwise, assume production environment variables are already set.
        """
        
        if os.getenv("ENV", "local").lower() != "production":
            load_dotenv()
            log.info("Running in LOCAL MODE: env loaded.")
        else:
            log.info("Running in PRODUCTION MODE!!!")

        self.api_key_manager = ApiKeyManager()
        self.config = load_config()
        log.info("YAML config loaded")


    def load_llm(self):
        """"
        load and return the configured LLM model
        """
        # dynamically pick which LLM provider to use based on the environment
        llm_block = self.config["llm"]
        provider_key = os.getenv("LLM_PROVIDER", "mistral") # If LLM_PROVIDER does not exist, it returns "mistral" (the default value).

        if provider_key not in llm_block:
            log.error(f"LLM provider not found in config provider={provider_key}")
            raise ValueError(f"LLM provide '{provider_key}' not found in config")

        llm_config = llm_block[provider_key]
        provider = llm_config.get("provider")
        model_name =  llm_config.get("model_name")
        temperature = llm_config.get("temperature", 0.2)

        if provider_key == "mistral":
            log.info(f"Loading LLM, provider={provider}, model={model_name}")
            return ChatMistralAI(
                model_name=model_name,
                temperature=temperature
            )
        else:
            log.error("Unsupported LLM provider", provider=provider)
            raise ValueError(f"Unsupported LLM provider: {provider}")

    def load_embedding(self):
        """
        load and return the configured embedding model
        """
        try:
            model_name = self.config["embedding_model"]["model_name"]
            # model_name = "mistral-embed"
            log.info(f"Loading embedding model, model={model_name}")
            embeddings = HuggingFaceEmbeddings(
                model_name=model_name
            )
            return embeddings
        except Exception as e:
            log.error(f"Error loading embedding model, error={str(e)}")
            raise ProjectException("Failed to load embedding model", sys)
        
    def load_mistral_embedding(self):
        """
        load and return the configured embedding model
        """
        try:
            # model_name = self.config["embedding_model"]["model_name"]
            model_name = "mistral-embed"
            log.info(f"Loading embedding model, model={model_name}")
            embeddings = MistralAIEmbeddings(
                model_name=model_name
            )
            return embeddings
        except Exception as e:
            log.error(f"Error loading embedding model, error={str(e)}")
            raise ProjectException("Failed to load embedding model", sys)







