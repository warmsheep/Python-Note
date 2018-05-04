from socket import*#在写socket可以这么写，一般情况下不这么写

sever=socket(AF_INET,SOCK_DGRAM)#udp协议，不存在粘包问题
sever.bind(("127.0.0.1",8080))

res1=sever.recvfrom(1)
print("第一次接收",res1)
res2=sever.recvfrom(1024)
print("第一次接收",res2)

sever.close()
#发数据，数据不安全
