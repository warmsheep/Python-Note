from socket import *

server=socket(AF_INET,SOCK_STREAM)
server.bind(("127.0.0.1",8080))
server.listen(5)

while True:
    conn,addr=server.accept()
    print(addr)

    while True:
        try:
            data=conn.recv(1024)
            if not data:break
            conn.send(data.upper())
        except ConnectionResetError:
            break
    conn.close()

server.close()
