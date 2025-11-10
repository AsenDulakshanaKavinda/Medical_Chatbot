import sys
from chatbot.logger import logging as log

def error_message_detail(error: Exception, error_details: sys):
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    message = f"Error in [{file_name}] at the line [{line_number}]: {str(error)}"
    log.error(message)
    return message


class ProjectException(Exception):
    def __init__(self, error_message: str, error_details: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_details)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        result = 10/0
    except Exception as e:
        ProjectException(error_message=str(e), error_details=sys)

