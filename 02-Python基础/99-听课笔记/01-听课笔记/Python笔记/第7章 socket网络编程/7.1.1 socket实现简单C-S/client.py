import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
hostname=socket.gethostname()
client.connect((hostname,8080))
client.send("hello".encode("utf-8"))
client.close()
