import socket               # Import socket module
import time
import random
import string

s = socket.socket()         # Create a socket object
host = '188.166.155.224' 	# Get local machine name
port = 8090                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    f = open(''.join(random.sample(string.ascii_letters + string.digits, 8)),'wb')
    print "Receiving..."
    l = c.recv(524288)
    while (l):
        print "Receiving..."
        f.write(l)
        l = c.recv(524288)
    f.close()
    print "Done Receiving"
    c.send('success')
    