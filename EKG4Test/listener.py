# -*- coding: utf-8 -*-

import socket
import sys
import json

from reporter import ReporterManager

HOST = '127.0.0.1'
PORT = 51116

class MessageParser(object):
    def __init__(self):
        self._valid = False
        self._completed = False
        self.data = ""

    def is_valid(self):
        return bool(self._valid and self._completed)

    def parse(self, data):
        if len(data) > 512:
            raise ValueError("data length exceed!")
        elif data.find("\n") >= 0:
            self._completed = True
            self.data += data.split('\n')[0]
            parsed = json.loads(self.data)
            if isinstance(parsed, dict):
                self._valid = ReporterManager.update(parsed.get("name"),
                                                     parsed.get("runner"),
                                                     parsed.get("success"),
                                                     parsed.get("failures"),
                                                     parsed.get("errors"))
            else:
                raise ValueError("Invalid input")
        self.data += data
    
    def is_completed(self):
        return self._completed
    
def get_socket():
    (af, socktype, proto, canonname, sa) = socket.getaddrinfo(HOST, PORT,
                                                              socket.AF_INET, socket.SOCK_STREAM,
                                                              0, socket.AI_PASSIVE)[0]
    try:
        sckt = socket.socket(af, socktype, proto)
        sckt.bind(sa)
        sckt.listen(1)
        return sckt
    except socket.error, msg:
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
            conn.send('ValueError')
            del mp; break
        if mp.is_valid(): del mp; break
    conn.close()
    listening(sckt)

def connect():
    listening(get_socket())
