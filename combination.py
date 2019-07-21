__copyright__ = """
Copyright (C) 2018-2019
MSP (Message Send Protocol)
Combination Part"""

from bath import certificate
from server import server
from server import handle_server
from server import DataTransport
from entrance import adress


class TCPServer(handle_server):
    def __init__(self):
        return(server(certificate()))
        
class MessageService(object):
    def __init__(self, *args):
        self.args = list({
        	'@0': None, 
        '@1': 1, 
        '@2': 2, 
        '@3': 3, 
        '@4': 4, 
        '@5': 5, 
        '@6': 6, 
        '@7': 7, 
        '@8': 8, 
        '@9': 9, 
        '@10': 10
        })
        DataTransport()['@1', 
        '@2', 
        '@3', 
        '@4', 
        '@5', 
        '@6', 
        '@7', 
        '@8', 
        '@9', 
        '@10']
        
class SendAdress(adress):
    def __init__(self):
        return(adress)

class CsExceptions(Exception):
    pass

