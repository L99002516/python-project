# import socket programming library 
import socket 
from unittestdemo import *
# import thread module 
from _thread import *
import threading 

print_lock = threading.Lock() 
Compare_list=[]
# thread function 
def threaded(c): 
	while True: 
		
		# data received from client 
		data = c.recv(1024) 
		if not data: 
			print('Bye') 
			
			# lock released on exit 
			print_lock.release() 
			break

		#checking the brand name or phone name  is present in our data or not
		#print(data.decode("utf-8"))
		for i in range(0,len(your_list)):
			if data.decode("utf-8") in your_list[i]:
				print(your_list[i])
				#c.send(your_list[i])
				Compare_list.append(your_list[i])
		count1=0
		count2=0
		#c.send(Compare_list.encode('ascii'))
		for i in range(0,len(Compare_list)):
			for j in range(3,len(Compare_list[i])-1):
				if Compare_list[i][j]>Compare_list[i+1][j]:
					count1=count1+1
				elif(Compare_list[i][j]==Compare_list[i+1][j]):
					continue
				else:
					count2=count2+1
			break
		if count1>count2:
			#c.send(Compare_list[0])
			print(Compare_list[0])
		else:
			#c.send(Compare_list[1])
			print(Compare_list[1])
				
		#print(Compare_list)
		# send back reversed string to client 
		
		c.send(data) 

	# connection closed 
	c.close() 


def Main(): 
	host = "" 

	# reverse a port on your computer 
	# in our case it is 12345 but it 
	# can be anything 
	port = 12345
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.bind((host, port)) 
	print("socket binded to port", port) 

	# put the socket into listening mode 
	s.listen(5) 
	print("socket is listening") 

	# a forever loop until client wants to exit 
	while True: 

		# establish connection with client 
		c, addr = s.accept() 

		# lock acquired by client 
		print_lock.acquire() 
		print('Connected to :', addr[0], ':', addr[1]) 

		# Start a new thread and return its identifier 
		start_new_thread(threaded, (c,)) 
	s.close() 


if __name__ == '__main__': 
	Main() 

