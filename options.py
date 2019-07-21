__copyright__ = """
Copyright (C) 2018-2019
MSP (Message Send Protocol)
Options (Combination Helper)"""

from message_text import UDP
from message_text import Text
import bath
import entrance
from entrance import adress
from entrance import class_name
from entrance import name
import exceptions
import server
from combination import SendAdress
import platform

class MSPMain(object):
    def __init__(self):
        def server_options(self):
        
            system = platform.system()
            
            if(system == 'Windows'):
                server.handle_server()
            
            else:
                server.server()
                
        def certificate_options(self):
        
            system = platform.system()
            
            if(system == 'Windows'):
                return(bath.certificate())
                
            else:
                return(bath.ssl.SIG_UNBLOCK(server))
                
        def data_options(self):
            server.DataTransport(Text)
            
        def adress_options(self):
            main = adress()
            
            if(main is None):
                SendAdress()
                
        def entrance_options(name):
            init_name = name(name)
            class_name(init_name)
                
        class MSPExceptions(Exception):
            def __init__(self):
            
                def MessageError(self):
                    return(exceptions.MessageError())
                    
                def AdressError(self):
                    return(exceptions.AdressError())
                    
                def classnameerror(self):
                    return(exceptions.classnameerror())
                    
                def CertificateError(self):
                    return(exceptions.CertificateError())




