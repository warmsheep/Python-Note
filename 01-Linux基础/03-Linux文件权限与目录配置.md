# 03-Linux文件权限与目录配置
## 03.1 使用者与群组
* 文件拥有者、群组、其他人的概念
* 关系可以用如下来解释（以王大毛为中心）
 ![每个文件的拥有者、群组与others的示意图](03-图片/每个文件的拥有者、群组与others的示意图.png)

* Linux 用户身份与群组记录的文件

| 名称 | 所在目录 |
|:-- |:-- |
| root相关信息 | /etc/passwd |
| 个人密码 | /etc/shadow |
| 组名 | /etc/group |

## 03.2 文件权限概念
### Linux文件属性
* 用ls -al 文件名查看：
```
[root@i-jjr0xl1a ~]# ls -al
total 32
dr-xr-x---.  2 root root 4096 Dec 25 01:20 .
dr-xr-xr-x. 18 root root 4096 Dec 29 14:15 ..
-rw-------   1 root root 1345 Dec 29 14:42 .bash_history
-rw-r--r--.  1 root root   18 Dec 29  2013 .bash_logout
-rw-r--r--.  1 root root  176 Dec 29  2013 .bash_profile
-rw-r--r--.  1 root root  176 Dec 29  2013 .bashrc
-rw-r--r--.  1 root root  100 Dec 29  2013 .cshrc
-rw-r--r--.  1 root root  129 Dec 29  2013 .tcshrc
```

| 权限 | 连结 | 拥有者 | 群组 | 文件容量 | 修改日期 | 档名|
|:-- |:-- |:-- |:-- |:-- |:-- |:-- |
| -rw------- | 1 |root|root|1345|Dec 29 14:42|.bash_history|
* 注意：这个文件容量是以byte为单位的，如果想要文件自适应大小，则可以用 ls -al -h 文件名这个命令。
```
[root@i-jjr0xl1a jun]# ls -al a.txt
-rw-r--r-- 1 root root 4113 Dec 29 15:46 a.txt
[root@i-jjr0xl1a jun]# ls -al -h a.txt
-rw-r--r-- 1 root root 4.1K Dec 29 15:46 a.txt
```
