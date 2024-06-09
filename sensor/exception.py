import sys # to capture the details of the Error
import os



def error_message_detail(error,error_detail:sys):
    # line number 
    # Konse file me error aarhi hai
    # which error is that
    
    _,_,exc_tb = error_detail.exc_info()
    # after exc_tb we will be finding the the above 3 aspects
    
    fileName=exc_tb.tb_frame.f_code.co_filename # what is the file name where error is occured.
    
    error_message ="Error occured and the file name is [{0}] and the lineNumber is [{1}] and error is [{2}]".format( fileName,exc_tb.tb_lineno,str(error))
    return error_message

class SensorException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        
        # To capture the error details 
        self.error_message =error_message_detail(error_message,error_detail=error_detail)

        
     # to convert the errors into string 
    def __str__(self):
         return self.error_message   
        
    