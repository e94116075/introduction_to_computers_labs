import socket 
HOST = '10.3.141.1'
PORT = 8000
a=True
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while a==True:
    print('connected to ' + str(HOST)+":"+str(PORT))
    while True:
        outdata = input('please input message: ')
        if str(outdata) == 'EXIT': # connection closed
            a=False
            s.close()
            print('closed connection.')
            break
        print('send: ' + outdata)
        s.send(outdata.encode())
    
        indata = s.recv(1024)
        
        print(indata.decode())
