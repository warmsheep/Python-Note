import socket
import subprocess
import json
import struct
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
hostname=socket.gethostname()
server.bind((hostname,8090))
server.listen(5)
while True:
    client,addr=server.accept()
    while True:
        cmd=client.recv(1024)
        if not cmd:break
        obj=subprocess.Popen(cmd,shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        stderr=obj.stderr.read()
        if stderr:
            ret=stderr
        else:
            ret=obj.stdout.read()
        #制作报头
        header_dic={
            "cmd":cmd.decode("utf-8"),
            "total_size":len(ret)
        }

        header_json=json.dumps(header_dic)
        header_bytes=bytes(header_json,encoding="utf-8")
        client.send(struct.pack("i",len(header_bytes)))
        client.send(header_bytes)
        client.send(ret)
    client.close()
server.close()
