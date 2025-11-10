import os
import sys
import json

from chatbot.logger import logging as log
from chatbot.exception import ProjectException


class ApiKeyManager:
    # list of api keys need
    REQUIRED_KEY = ["MISTRAL_API_KEY", "PINECONE_API_KEY"]

    def __init__(self):
        self.api_keys = {}

        # if .env has -> a dict of api keys
        raw = os.getenv("apikeys")
        if raw:
            try:
                parsed = json.loads(raw)
                if not isinstance(parsed, dict):
                    raise ValueError("apikeys is not a valid json object")
                self.api_keys = parsed
                log.info("Loading apikeys from ECS secrets")
            except Exception as e:
                log.error(f"Faild to parse API KEYS as JSON error: {str(e)}")
                raise ProjectException("Faild to parse API KEYS as JSON", sys)


        # if .env has individual api key
        for key in self.REQUIRED_KEY:
            if not self.api_keys(key):
                env_val = os.getenv(key)
                if env_val:
                    self.api_keys[key] = env_val
                    log.info(f"Loaded {key} from individual env var.")

        # check for missing keys
        missing = [k for k in self.REQUIRED_KEY if not self.api_keys.get(k)]
        if missing:
            for k in missing:
                log.error(f"Missing required API key, missing key: {k}")
                raise ProjectException("Missing API keys", sys)
        
        log.info("API keys loaded.")













