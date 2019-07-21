__copyright__ = """
Copyright (C) 2018-2019
MSP (Message Send Protocol)
Exceptions Part"""

import message_text
import entrance
from entrance import class_name
from entrance import adress
import server
import bath

class MessageError(Exception):
    def __init__(self):

        if(message_text.Message is None):
            raise('enter not the message text')
            
class AdressError(Exception):
    def __init__(self):
        if(adress is None):
            raise('enter not the receipient adress')
            
        elif(adress is False or adress is not True):
            raise('false receipient adress')
            
class classnameerror(Exception):
    def __init__(self):
        if(class_name is None):
            raise('enter not the receipient adress')
            
        elif(class_name is False or adress is not True):
            raise('false receipient adress')
            
class CertificateError(Exception):
    def __init__(self):
        certifi = bath.certificate()
        
        if(certifi is None):
            raise('server certificate adapter is none')
            



