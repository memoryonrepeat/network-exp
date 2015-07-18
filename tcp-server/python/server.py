#!/usr/bin/env python 

import socket

HOST = ''
PORT = 9999

# Construct a server socket using AF_INET (IPv4) protocol and STREAM type (TCP-like)
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((HOST,PORT))

# Can queue up at most 5 connection requests at 1 time
serversocket.listen(1)

while 1:

	# Allocate a "client socket" for server when new connection comes in
	# This corresponds to the socket on the client side
	# Therefore, the main duty of the server socket is to manipulate its own client sockets
	(clientsocket,addr) = serversocket.accept()

	data = clientsocket.recv(1024)
	if data:
		print 'Connected by',addr
		clientsocket.send(msg)
	clientsocket.close()