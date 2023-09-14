import sys
from src.logger import logging


def error_message_details(error,error_detail:sys):
    _,_,error_tb = error_detail.exc_info()

    file_name = error_tb.tb_frame.f_code.co_filename
    line_no = error_tb.tb_lineno

    error_message ="Error has occured in the script of [{0}] in the line number [{1}] and the error is [{2}]".format(
        file_name, line_no, str(error))
    return error_message

class CustomException(Exception):
    def __init__(self,error,error_detail:sys):
        super(CustomException,self).__init__()
        self.error_message = error_message_details(error,error_detail)

    def __str__(self):
        return self.error_message


if __name__=="__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by Zeror error")
        raise CustomException(e,sys)