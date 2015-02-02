#!/usr/bin/env python
# coding: utf-8
# Copyright 2013 Abram Hindle
# 
# httpclient.py: I, Kevin Joseph De Asis have modified server.py,
# which is a partially HTTP 1.1 compliant HTTP Client that can GET 
# and POST to a webserver.
# Copyright 2015 Kevin Joseph De Asis 

#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Do not use urllib's HTTP GET and POST mechanisms.
# Write your own HTTP GET and POST
# The point is to understand what you have to send and get experience with it
#
# The basis of learning sockets was obtained from 
# http://www.binarytides.com/python-socket-programming-tutorial/
# Python socket – network programming tutorial
# By Silver Moon 

import sys
import socket
import re
# you may use urllib to encode data appropriately
import urllib
from urlparse import urlparse

def help():
    print "httpclient.py [GET/POST] [URL]\n"

class HTTPRequest(object):
    def __init__(self, code=200, body=""):
        self.code = code
        self.body = body

class HTTPClient(object):
    #def get_host_port(self,url):

    def connect(self, host, port):
        # use sockets!
        #socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #socket_.connect((host , 80))
        
        
        return none

    def get_code(self, data):
        return None

    def get_headers(self,data):
        return None

    def get_body(self, data):
        return None

    # read everything from the socket
    def recvall(self, sock):
        buffer = bytearray()
        done = False
        while not done:
            part = sock.recv(1024)
            if (part):
                buffer.extend(part)
            else:
                done = not part
        return str(buffer)

    def GET(self, url, args=None):
        code = 500
        body = ""
        
        addresshostname_ = urlparse(url).hostname
        addressport_ = urlparse(url).port
        addresspath_ = urlparse(url).path
                
        if addressport_:
            #connection = self.connect(addresshostname_, addressport_)
            
            socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_.connect((addresshostname_ , addressport_))            
        else:
            #connection = self.connect(addresshostname_, 80)
            
            socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_.connect((addresshostname_ , 80))              
            
        message = "GET "+addresspath_+" HTTP/1.1\r\nHost: "+addresshostname_+"\r\n\r\n"
        
        print(message)
        socket_.send(message)
        print("here1")
        
        reply = self.recvall(socket_)
        print("here2")
        
        code = int(((reply.split("\r\n"))[0]).split()[1])
        print "exit"
        body = (reply.split("\r\n\r\n"))[1]
        
        print code
        print "code"
        print body
        print "body"

        return HTTPRequest(code, body)

    def POST(self, url, args=None):
        code = 500
        body = ""
        
        addresshostname_ = urlparse(url).hostname
        addressport_ = urlparse(url).port
        addresspath_ = urlparse(url).path
                
        if addressport_:
            #connection = self.connect(addresshostname_, addressport_)
            
            socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_.connect((addresshostname_ , addressport_))            
        else:
            #connection = self.connect(addresshostname_, 80)
            
            socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_.connect((addresshostname_ , 80))              
            
        message = "POST "+addresspath_+" HTTP/1.1\r\nHost: "+addresshostname_+"\r\n\r\n"
        
        print(message)
        socket_.send(message)
        print("here1")
        
        reply = self.recvall(socket_)
        print("here2")
        
        code = int(((reply.split("\r\n"))[0]).split()[1])
        print "exit"
        body = (reply.split("\r\n\r\n"))[1]
        
        print code
        print "code"
        print body
        print "body"

        
        return HTTPRequest(code, body)

    def command(self, url, command="GET", args=None):
        if (command == "POST"):
            return self.POST( url, args )
        else:
            return self.GET( url, args )
    
if __name__ == "__main__":
    client = HTTPClient()
    command = "GET"
    if (len(sys.argv) <= 1):
        help()
        sys.exit(1)
    elif (len(sys.argv) == 3):
        print client.command( sys.argv[1], sys.argv[2] )
    else:
        print client.command( command, sys.argv[1] )    
