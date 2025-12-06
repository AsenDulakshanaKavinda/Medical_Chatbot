
import os

import logging
from logging.handlers import RotatingFileHandler


def get_logger(name: str = "Medical-Chatbot"):

    """ 
    Create a logger instance 

    - Use

        logger = get_logger()
        
        logger.info("Log message.")
    """
    logger = logging.getLogger(name=name)

    if not logger.handlers:
        # set-up console handler
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

        # file handler with rotation (max 3MB, keep 3 backups)
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)
        file_handler = RotatingFileHandler('logs/app.log', maxBytes=3*1024*1024, backupCount=3)
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

        # set logger level
        logger.setLevel(logging.DEBUG)

    return logger

logger = get_logger()