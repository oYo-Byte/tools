import socket               # Import socket module
import time

        
host = '188.166.155.224' 	# Get local machine name
port = 8090                 # Reserve a port for your service.

count = 10
total_diff = 0
for i in xrange(count):
    t0 = time.time()
    s = socket.socket() 	# Create a socket object
    s.connect((host, port))
    f = open('testfile.dat','rb')
    l = f.read(524288)
    while (l):
        s.send(l)
        l = f.read(524288)
    f.close()
    s.shutdown(socket.SHUT_WR)
    print s.recv(1024)
    t_diff = time.time() - t0
    s.close
    print "socket transfer use time: %s" % t_diff
    total_diff += t_diff
    time.sleep(120)
	
print "socket transfer total time: %s" %  total_diff
