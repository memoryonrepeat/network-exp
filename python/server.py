import socket
HOST = ''
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Created server socket'
s.bind((HOST,PORT))
s.listen(1)
(conn,addr) = s.accept()
print 'Connected by',addr
while 1:
	data = conn.recv(1024)
	if not data:
		break
	conn.sendall(data)
conn.close()