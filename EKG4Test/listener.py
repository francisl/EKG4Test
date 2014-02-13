#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys

HOST = '127.0.0.1'
PORT = 51116

class MessageParser(object):
    def __init__(self):
        self.name = None
        self.runner = None
        self.failed = None
        self.succeed = None
        self.completed = False

    def is_valid(self):
        if (self.name is None or self.runner is None or self.failed is None or self.succeed is None):
            return False
        return True

    def parse(self, data):
        if data.find("\n") > 0:
            self.completed = True            
    
    def is_completed(self):
        return self.completed
    
def get_socket():
    (af, socktype, proto, canonname, sa) = socket.getaddrinfo(HOST, PORT,
                                                              socket.AF_UNSPEC, socket.SOCK_STREAM,
                                                              0, socket.AI_PASSIVE)[0]
    try:
        sckt = socket.socket(af, socktype, proto)
        sckt.bind(sa)
        sckt.listen(1)
        return sckt
    except socket.error, msg:
        sckt.close()
        sys.exit(1)


def listening(conn):
    mp = MessageParser()
    while 1:
        data = conn.recv(512)
        if not mp.is_valid(): return
        conn.send(data)

def connect():
    (conn, addr) = get_socket().accept()
    listening(conn)
    conn.close()
    connect()
