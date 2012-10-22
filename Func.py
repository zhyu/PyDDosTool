# -*- coding: utf-8 -*-

import socket, threading

def getIP(domainName):
    return socket.gethostbyname(domainName)
        