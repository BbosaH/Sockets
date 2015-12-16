import socket
import select
class seriousServer :
	def __init__(self,port) :
		self.port = port;
		self.srverSocket = socket.socket( socket.AF_INET,socket.SOCK_STREAM);
		self.srverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1);
		self.srverSocket.bind(("localhost",port));
		self.srverSocket.listen(5);
		self.descriptors=[self.srverSocket];
		print ("chat server started at port %s"%port);
	#----------------------------------------------------------------------
	def run(self):
		while 1:
			(sread,swrite,sexc) = select.select(self.descriptors,[],[]);
			for sock in sread:
				if sock == self.srverSocket :
					self.accept_new_connection()
				else:
					strr=sock.recv(100);
					if strr=="":
						host,port = sock.getpeername();
						strr = "client left %s:%s\r\n" %(host,port)
						self.broadcast_string(strr,sock);
						sock.close()
						self.descriptors.remove(sock)
					else:
						host,port = sock.getpeername()
						newstr = "[%s:%s]%s" %(host,port,strr)
						self.broadcast_string(newstr,sock)
	#----------------------------------------------------------------------
	def accept_new_connection(self):
		newsock,(remhost,remport)=self.srverSocket.accept();
		self.descriptors.append(newsock);
		newsock.send("you are connected to python chatsServer")
		sttr = "client joines @ %s:%s \r \s" %(remhost,remport);
		self.broadcast_string(sttr,newsock);
	#----------------------------------------------------------------------
	def broadcast_string(self,strr,omit_sock):
		for sock in self.descriptors:
			if sock !=omit_sock  and sock != self.srverSocket:
				sock.send(strr)
		print(strr);		
		
myserver=seriousServer(8080);		
myserver.run();
		
		
