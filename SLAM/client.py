#!/usr/bin/env python
# coding: utf-8

import socket
host = "127.0.0.1"
port = 15555
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((host,port))
print "Connection on {}".format(port)
msg = "Hey my name is Olivier!"
socket.send(msg.encode())
print "Close"
socket.close