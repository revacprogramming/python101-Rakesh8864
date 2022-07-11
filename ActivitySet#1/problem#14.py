# Object Oriented Programming
# https://www.py4e.com/lessons/Objects
from socket import

soc = socket(AF_INET,SOCK_STREAM)
soc.connect(("data.py4e.org",80))
cmd = "get http://data.py4e.org/intro-short.txt HTTP/1.0\r\n\r\n".encode()
soc.send(cmd)

while TRue:
    data =soc.recv(512)
    if(len(data)<1):
       break
    print(data.decode())
soc.close()