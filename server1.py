import socket 
from _thread import *
import threading 
from unittestdemo import *


print_lock = threading.Lock() 
Compare_list=[]
def threaded(c): 
	while True: 
		data = c.recv(1024) 
		if not data: 
			print('Bye') 
			
			print_lock.release() 
			break
		for i in range(0,len(your_list)):
			if data.decode("utf-8") in your_list[i]:
				print(your_list[i])
				Compare_list.append(your_list[i])
		count1=0
		count2=0
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
			print(Compare_list[0])
		else:
			print(Compare_list[1])
		c.send(data) 
	c.close() 


def Main(): 
	host = "" 

	port = 12345
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.bind((host, port)) 
	print("socket binded to port", port) 
	s.listen(5) 
	print("socket is listening") 

	while True: 

		c, addr = s.accept() 

		print_lock.acquire() 
		print('Connected to :', addr[0], ':', addr[1]) 

		start_new_thread(threaded, (c,)) 
	s.close() 


if __name__ == '__main__': 
	Main() 

