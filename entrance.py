__copyright__ = """
Copyright (C) 2018-2019
MSP (Message Send Protocol)
Server Register Adapter"""

import reprlib
import hashlib
import server
from message_text import Text
import getpass
import socket
import json

def name(name):
    return(unicode(name))

class QHac(object):
    def __init__(self):
        def actor_name(name):
            self.name = name
            handle_name = repr(getpass.getuser())
            return(json.loads({'name' : handle_name, 
            'root' : name(name)}))
        
class class_name():
    def __unicode__(self):
        self.name = name
        origin_name = name(self.name.encode('utf-8'))
        
        def text(msg1, msg2):
            s = socket.socket()
            s.send(name.encode())
            s_id = s.recv(1024)
            s_name = s_id.decode()
            
            while 1:
                message = s.recv(1024)
                message = message.decode()
                message = ''' {}
{}'''.format(msg1, msg2)

                message = message.encode()
                s.send(message)
                
        return(QHac().actor_name(origin_name)['root'])
        
class adress(socket.socket):
    def __init__(self):
        s = socket.socket()
        
        def adress_name(self, name):
            s.send(name.encode())
        
if(__name__ == '__main__'):
    try:
        class_name()
        print('entrance user succes')
    except:
        print('@ERROR: do not found an user')



