#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys

HOST = '127.0.0.1'
PORT = 51116


def get_socket():
    (af, socktype, proto, canonname, sa) = socket.getaddrinfo(HOST, PORT,
                                                              socket.AF_UNSPEC, socket.SOCK_STREAM,
                                                              0, socket.AI_PASSIVE)[0]
    try:
        print("trying")
        sckt = socket.socket(af, socktype, proto)
        sckt.bind(sa)
        return sckt.listen(1)
    except socket.error, msg:
        sckt.close()
        print 'could not open socket'
        sys.exit(1)


def listening(conn):
    while 1:
        print("looping")
        data = conn.recv(1024)
        print("data : %s" % data)
        if not data:
            break
        conn.send(data)
    
def connect():
    (conn, addr) = get_socket().accept()
    listening(conn)
    conn.close()
    connect()

connect()