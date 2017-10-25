#coding=utf-8
import socket
import generator
import re
import os
import threading
HOST = '127.0.0.1'
PORT = 9999

#configure socket


def link(connection, address):
	global path
	request = connection.recv(1024).decode('utf-8')
	method = request.split(' ')[0]
	src = request.split(' ')[1]
	
	# print('connect by ', address)
	# print('Request is:\n', request)
	# print('src is', src)
	# print('method is', method)
	
	if method == 'GET':
			if src == '/css/img/vertical-waves.jpg':
				content = generator.get_img()
		
			elif src == '/':
				path = '.'
				content = generator.get_content(path)
			
			elif src == '/up':
				path += '/..'
				content = generator.get_content(path)
			elif re.match(r"^/[A-Za-z0-9\.\_]+$", src):
				if os.path.isdir(os.path.join(path, src[1:])):
					path += src
					content = generator.get_content(path)
				else:
					if os.path.isfile(os.path.join(path, src[1:])):
						path += src
						content = generator.get_file(path)
					else:
						content = generator.get_404()
			elif src == '/css/decoration.css':
				content = generator.get_css()
			
			else:
				content = generator.get_404()
				
			
			connection.sendall(content)
			connection.close()
			

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(100)

path = '.'
while True:
	connection, address = sock.accept()
	t = threading.Thread(target=link, args=(connection, address))
	t.start()
















