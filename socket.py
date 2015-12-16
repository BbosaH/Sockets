import socket
class sockket:
	def __init__(self,port):
                        self.tcpnocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
                        self.tcpnocket.connect(("localhost",port));#TCP/IP SOCKET
		#datagramsocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM);#DATAGRAM SOCKET
		# AF_INET= IPv4 protocol socket,AF_INET6= IPv6 protocol socket
		
		#tcpsocket.close(); #closing socket
		#del  tcpsocket; #deleting socket.. permanetly removes socket object..invoking it after causes error.
mysock=sockket(8080);
