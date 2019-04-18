from socket import *
import sys
import threading

# function for receiving messages from server
def recv_from_server(conn):
	global FLAG
	
	while True:
		# Receives the request message from the client
		message = conn.recv(1024).decode()
		
		# if there is message received print it
		if message:
			print('Message Received: ' + message)

# function for sending messages to server
def send_to_server(clsock):
	while True:
		send_msg = input('Type Message: ')
		clsock.sendall(send_msg.encode())


# this is main function
def main():
	# Host name or ip address
    HOST = 'localhost'
	# PORT numbers, one is for sending and one is receiving 
    PORT = 65535 
    PORT2 = 65534

	# 2 TCP sockets one is using for sending and one is used for receiving
    receivingSocket = socket(AF_INET, SOCK_STREAM)
    sendingSocket = socket(AF_INET, SOCK_STREAM)
	
	# Bind the socket to port
    sendingSocket.bind(('', PORT2))

	# request a connection to the server
    receivingSocket.connect((HOST, PORT))
	
	# listen to for server and wait for request
    sendingSocket.listen(1)
    connectionSocket, addr = sendingSocket.accept()
	
    print('Client is connected to a chat server!\n')
	
	# 2 threads for listening and receiving, these will run simultaneously
    sendingThread = threading.Thread(target = send_to_server, args = (receivingSocket,))
    receivingThread = threading.Thread(target = recv_from_server, args = (connectionSocket,))
	
	# start the threads
    sendingThread.start()
    receivingThread.start()
	
# This is where the program starts
if __name__ == '__main__':
    main()
