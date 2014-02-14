#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
import json

HOST = '127.0.0.1'
PORT = 51116

class MessageParser(object):
    def __init__(self):
        self.name = None
        self.runner = None
        self.failed = None
        self.succeed = None
        self.completed = False
        self.data = ""

    def _set_info(self, data):
        self.name = data.get("name")
        self.runner = data.get("runner")
        self.failed = data.get("failed")
        self.succeed = data.get("succeed")

    def is_valid(self):
        return not (self.name is None or
                    self.runner is None or
                    self.failed is None or
                    self.succeed is None)

    def parse(self, data):
        if len(data) > 512:
            raise ValueError("data length exceed!")
        elif data.find("\n") > 0:
            self.completed = True
            self.data += data.split('\n')[0]
            parsed = json.loads(self.data)
            if isinstance(parsed, dict):
                self._set_info(parsed)

        self.data += data
    
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
        print("msg : %s" % msg)
        sckt.close()
        sys.exit(1)


def listening(sckt):
    (conn, addr) = sckt.accept()
    mp = MessageParser()
    while 1:
        data = conn.recv(1024)
        if not data: break
        try:
            mp.parse(data)
        except ValueError:
            del mp; break
        if mp.is_valid(): del mp; break
    conn.close()
    listening(sckt)

def connect():
    listening(get_socket())
