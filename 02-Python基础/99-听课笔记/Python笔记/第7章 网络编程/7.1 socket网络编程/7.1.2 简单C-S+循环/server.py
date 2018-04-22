import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
hostname=socket.gethostname()
server.bind((hostname,8080))
server.listen(5)
while True:
    client,addr=server.accept()
    while True:
        res=client.recv(1024)
        if not res:break
        print(res)
        client.send(res.upper())

client.close()
server.close()
