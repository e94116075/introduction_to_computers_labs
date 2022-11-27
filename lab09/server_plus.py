import socket,threading,sys,errno
from signal import signal, SIGPIPE, SIG_DFL 
signal(SIGPIPE,SIG_DFL) 

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("connected by ", clientAddress)
    def run(self):
        a=True
        while a==True:
            indata = self.csocket.recv(1024)
            if len(indata)==0:
                a=False
                break
            print(str(clientAddress)+":"+indata.decode())
            outdata = 'echo: ' + indata.decode()
            self.csocket.send(outdata.encode())
        print(str(clientAddress)+'closed connection.')

HOST = '10.3.141.1'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))

print('server start at: %s:%s' % (HOST, PORT))   
while True:
    print('wait for connection...')
    s.listen(1)
    clientsock, clientAddress = s.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()

