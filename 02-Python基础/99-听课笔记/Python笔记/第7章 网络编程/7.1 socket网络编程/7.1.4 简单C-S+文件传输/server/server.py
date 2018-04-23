import socket
import subprocess
import json
import struct
import os
import sys
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
hostname=socket.gethostname()
server.bind((hostname,8090))
server.listen(5)
path=os.getcwd()
print(path)
share_dir=path+"/server/share"
print(share_dir)


def get(client,cmds):
    filename = cmds.split()[1]
    print(filename)
    # 制作报头
    header_dic = {
        "filename": filename,
        "file_size": os.path.getsize("%s/%s" % (share_dir, filename))
    }

    header_json = json.dumps(header_dic)
    header_bytes = header_json.encode("utf-8")
    client.send(struct.pack("i", len(header_bytes)))
    client.send(header_bytes)
    with open("%s/%s" % (share_dir, str(filename)), "rb") as f:
        for line in f:
            client.send(line)

while True:
    client,addr=server.accept()
    while True:
        try:
            cmd=client.recv(8096)
            if not cmd:break
            cmds=cmd.decode("utf-8")
            if cmds.split()[0]=="get":
                get(client,cmds)

        except ConnectionResetError:
            break

    client.close()
server.close()
