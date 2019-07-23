#Updated : 27/07/2019
__copyright__ = """
Copyright (C) 2018-2019
MSP (Message Send Protocol)
Server Security Adapter"""

import os
import ssl
import server
import socket
import logging

logging.basicConfig(level = logging.INFO)

class certificate(object):
    def __init__(self):
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        context.load_verify_locations('data/certificate/context.ssl')
        
        def security():
            _create_unverified_https_context = ssl._create_unverified_context
            ssl._create_default_https_context = _create_unverified_https_context
            return(os.system('ping'+str(server.server()))



