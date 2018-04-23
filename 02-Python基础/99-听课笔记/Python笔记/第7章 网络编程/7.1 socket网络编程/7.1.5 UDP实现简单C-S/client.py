import socket
cilent=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#udp协议，不存在粘包问题

cilent.sendto(b"hello",("127.0.0.1",8080))
cilent.sendto(b"world",("127.0.0.1",8080))

cilent.close()
