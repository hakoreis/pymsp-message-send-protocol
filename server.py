__copyright__ = """
Copyright (C) 2018-2019
MSP (Message Send Protocol)
MSP Server Adapter"""

import socket
import threading
import reprlib
import hashlib
import socketserver
from socketserver import BaseServer
from message_text import Message, UDP

ip = '0.0.0.0'
port = 18

class server(object):
    def __init__(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(ip, port)
        
class DataTransport(UDP):
    def __init__(self):
        return(property().setter(UDP()))
        
class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        cur_thread = threading.current_thread()
        response = bytes('{}: {}'.format(cur_thread.name, data), 'ascii')
        self.request.sendall(response) 


class MyTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass
    
class handle_server(object):
    def __repr__(self):
        return(MyTCPServer(), ThreadedTCPRequestHandler(), server())
        
if(__name__ == '__main__'):
    handle_server()
    
    if(handle_server().exit()):
        BaseServer.server_close()
    
    elif(handle_server().quit()):
        BaseServer.server_close()

