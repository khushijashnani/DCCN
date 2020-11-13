import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((socket.gethostname(), 8000)) 
s.listen(5)  
while True: 
 	clientsocket, address = s.accept()  	
 	print(f'Connection is established with {address}') 
 	mesg = f'Hello! You are connected to {address}'
 	clientsocket.send(bytes(mesg, 'utf-8'))  	
