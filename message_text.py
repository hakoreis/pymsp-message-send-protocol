__copyright__ = """
Copyright (C) 2018-2019
MSP (Message Send Protocol)
Message Text Document Adapter"""

import textwrap
import string
import argparse
import hashlib

def Text(msg1, msg2):
    msg1 = '\n' + msg1
    textwrap.TextWrapper.wrap(msg1)
    textwrap.TextWrapper.wrap(msg2)
    

class Message(object):
    def __str__(self):
        self.msg = type(str())
        
class UDP(object):
    def __init__(self):
        
        @property()
        def datagram(data):
            return(property().getter(data))
            
    def __setattr__(self, name, msg1, msg2):
        self.__dict__[name] = Text(msg1, msg2).upper()
            
    def __getattr__(self, name, msg1, msg2):
        __setattr__(self, name, msg1, msg2).value = Text(msg1, msg2)
        return(property().getter(__setattr__(self, name, msg1, msg2)))
        
        

