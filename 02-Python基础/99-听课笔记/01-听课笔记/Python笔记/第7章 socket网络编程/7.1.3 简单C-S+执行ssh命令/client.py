import socket
import json
import struct

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
hostname=socket.gethostname()
client.connect((hostname,8090))
while True:
    cmd=input(">>:").strip()
    if not cmd:continue
    client.send(cmd.encode("utf-8"))
    header_length=struct.unpack("i",client.recv(4))[0]
    header_bytes=client.recv(header_length)
    header_json=header_bytes.decode("utf-8")
    header_dic=json.loads(header_json)
    print(header_dic)
    total_size=header_dic["total_size"]
    print(type(total_size))
    recv_data=b""
    recv_size=0
    while recv_size < total_size:
        res=client.recv(1024)
        recv_data+=res
        recv_size+=len(res)
    print(recv_data.decode("utf-8"))
client.close()
