# Jacky Huynh
# 301305184

# Import socket module
from socket import *
import sys # In order to terminate the program
import threading

#FLAG = False  # this is a flag variable for checking quit

# function for receiving message from client
def recv_from_client(conn):
	global FLAG
	
	while True:
		# Receives the request message from the client
		message = conn.recv(1024).decode()
		# if there is a message received print it
		if message:
			print('Message Received: ' + message)

# function for sending messages to cleint
def send_to_client(clsock):
	while True:
		send_msg = input('Type Message: ')
		clsock.sendall(send_msg.encode())
	

# this is main function
def main():
	global FLAG
	global receivingThread
	global sendingThread

	# Host name or ip address
	HOST = 'localhost'
	# PORT numbers, one is for sending and one is receiving 
	serverPort = 65535
	serverPort2 = 65534
	
	# 2 TCP sockets one is using for sending and one is used for receiving
	sendingSocket = socket(AF_INET, SOCK_STREAM)
	receivingSocket = socket(AF_INET, SOCK_STREAM)
	
	# Bind the socket to server address and server port
	# bind the socket for HOSR and serverPort
	sendingSocket.bind(('', serverPort))
	
	# Listen to at most 1 connection at a time
	# listen and wait for request from client
	sendingSocket.listen(1)

	# Server should be up and running and listening to the incoming connections
	print('The chat server is ready to connect to a chat client')
	# accept any connection request from a client
	connectionSocket, addr = sendingSocket.accept()
	
	# request connection to client, and get client's receiving socket
	receivingSocket.connect((HOST, serverPort2))
	
	print('Server is connected with a chat client\n')
	
	# 2 threads for listening and receiving, these will run simultaneously
	receivingThread = threading.Thread(target = recv_from_client, args = (connectionSocket,))
	sendingThread = threading.Thread(target = send_to_client, args = (receivingSocket,))

	# start the threads
	receivingThread.start()
	sendingThread.start()
	
	#Terminate the program after sending the corresponding data
	sys.exit()


# This is where the program starts
if __name__ == '__main__':
	main()
