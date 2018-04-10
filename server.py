import socket
import _thread
import signal

def threadWork(client):
    while True:
        msg = client.recv(1024)
        if not msg:
            pass
        else:
            print('client send: {}'.format(msg.decode()))
            client.send('Tai Kuo'.encode())
    client.close()

PORT = int(input('server port:'))
HOST = '140.113.121.81'

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except msg:
    sys.stderr.write("[ERROR] : %s\n" % msg[1])
    sys.exit(1)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # reuse
s.bind( (HOST, PORT) )
s.listen(5)

print('server start {}:{}'.format(HOST, PORT))

def sigint(sig, frame):
    print("123")
    s.close()
    sys.exit(0)

signal.signal(signal.SIGINT, sigint)

while True:
    client_fd, client_addr = s.accept()
    print('client {} connected'.format(client_addr))
    _thread.start_new_thread(threadWork, (client_fd,))
s.close()
