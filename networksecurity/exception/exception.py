import sys
from networksecurity.logging import logger

class NetworksecurityException(Exception):
    def __init__(self, error_message, error_detail=sys):
        self.error_message = error_message
        _, _, exec_tb = error_detail.exc_info()

        self.lineno = exec_tb.tb_lineno
        self.file_name = exec_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occurred in script [{self.file_name}] at line [{self.lineno}] with message: {str(self.error_message)}"


if __name__ == '__main__':
    try:
        logger.logging.info("Enter the try block")
        a = 1 / 0  # This will raise ZeroDivisionError
    except Exception as e:
        raise NetworksecurityException(e, sys)
