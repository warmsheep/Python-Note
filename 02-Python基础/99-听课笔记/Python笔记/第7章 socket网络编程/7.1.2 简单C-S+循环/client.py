import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
hostname=socket.gethostname()
client.connect((hostname,8080))
while True:
    inp=input(">>:").strip()
    if not inp:continue
    client.send(inp.encode("utf-8"))
    res1=client.recv(1024)
    print(res1.decode("utf-8"))
client.close()
