import socket
import json
import struct
import os
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
hostname=socket.gethostname()
client.connect((hostname,8090))

path=os.getcwd()
print(path)
download_dir=path+"/download"
print(download_dir)

def get(client,cmds):
    filename=cmds[1]
    header_length=struct.unpack("i",client.recv(4))[0]
    header_bytes=client.recv(header_length)
    header_json=header_bytes.decode("utf-8")
    header_dic=json.loads(header_json)
    print(header_dic)
    total_size=header_dic["file_size"]
    with open("%s/%s" % (download_dir, filename), "wb") as f:
        recv_size = 0
        while recv_size < total_size:
            line=client.recv(1024)
            f.write(line)
            recv_size+=len(line)
            print("总大小: %s,已下载大小: %s"%(total_size,recv_size))


while True:
    cmd=input(">>:").strip()
    if not cmd:continue
    client.send(cmd.encode("utf-8"))
    cmds=cmd.split()
    if cmds[0]=="get":
        get(client,cmds)

client.close()
