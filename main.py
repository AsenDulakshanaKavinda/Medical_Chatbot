from src.medical_chatbot.core.logger_config import logger as log
from src.medical_chatbot.core.exception_config import ChatbotException

try:
    result = 10/0
except Exception as e:
    ChatbotException(
        e,
        context={"operation": "division_test", "value": 10}
    )



