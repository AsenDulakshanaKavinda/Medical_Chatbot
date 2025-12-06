import sys
import traceback
from typing import Optional, Any, Dict
from src.medical_chatbot.core.logger_config import logger

def format_error_message(error: Exception, tb) -> str:
    """
    Create a detaild, readble error message.
    - Args:

        error: Exception - the exception instance.
        tb: Any - the traceback object.

    - Return
            
        error_message: str - Formatted error message with filename, line number and error text.

    """

    # if no traceback get it from sys
    if tb is None: 
        exc_type, exc_val, exc_tb = sys.exc_info()
        tb = exc_tb

    # if again no traceback return a message
    if tb is None:
        return f"Error {str(error)} (no traceback available)."
    
    # get filename, linenumber and fulltrace of the error
    file_name = traceback.extract_tb(tb)[-1].filename
    line_number = traceback.extract_tb(tb)[-1].lineno
    full_trace = ''.join(traceback.format_tb(tb))

    error_message = f"Error in [{file_name}] at line [{line_number}]: {str(error)} \nFull Traceback:\n{full_trace}"

class ChatbotException(Exception):
    """
    Custome exception class providing detailed, logged error information.

    - Args:

        error: Exception - The original exception.
        context: Optional[Dict[str, Any]] - Optional extra information
        reraise: bool - If True, re-reaise after logging (default: False)
    
    - Use

        try:
            result = 10/0
        except Exception as e:
            ChatbotException(
                e,
                context = {"operation": "division_test", "value": 10},
                reraise = False
            )
    """

    def __init__(self, error: Exception, *, context: Optional[Dict[str, Any]], reraise: bool = False):
        exc_type, exc_val, exc_tb = sys.exc_info()
        self.context = context or {}

        # fromat message
        self.error_message = format_error_message(error=error, tb=exc_tb)


        # include context in message for debugging
        if self.context:
            self.error_message += f" | Context: {self.context}"
        

        # log the error with full traceback
        logger.error(msg=self.error_message, exc_info=True)

        # store original exception
        self.original_exception = error

        super().__init__(self.error_message)

        if reraise:
            raise self

    # str error message  
    def __str__(self):
        return self.error_message











