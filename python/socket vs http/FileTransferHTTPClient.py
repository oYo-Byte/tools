import requests
import time

#http://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file

url = "http://188.166.155.224:5000/"

count = 10
total_diff = 0
for i in xrange(count):
    t0 = time.time()
    fin = open('testfile.dat', 'rb')
    files = {'file': fin}
    try:
        r = requests.post(url, files=files)
        print r.text
    finally:
        fin.close()
    t_diff = time.time() - t0
    print "http transfer use time: %s" % t_diff
    total_diff += t_diff
    time.sleep(20)


print "http transfer total time: %s" %  total_diff