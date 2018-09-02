from socket import *

server=socket(AF_INET,SOCK_STREAM)
server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server.bind(("127.0.0.1",8080))
server.listen(5)
server.setblocking(False)#所有的变为非阻塞


rlist=[]
wlist=[]

while True:
    try:
        conn,addr=server.accept()
        rlist.append(conn)
        print(rlist)

    except BlockingIOError:


        #收消息
        del_rlist = []
        for conn in rlist:
            try:
                data=conn.recv(1024)
                if not data:
                    del_rlist.append(conn)
                    continue
                wlist.append((conn,data.upper()))#存放套接字以及套接字准备发送的东西
            except BlockingIOError:
                continue
            except Exception:
                conn.close()
                del_rlist.append(conn)

        #发消息
        del_wlist=[]
        for item in wlist:
            try:
                conn=item[0]
                data=item[1]
                conn.send(data)
                del_wlist.append(item)
            except BlockingIOError:
                pass

        for item in del_wlist:
            wlist.remove(item)

        for conn in del_rlist:
            rlist.remove(conn)

server.close()
