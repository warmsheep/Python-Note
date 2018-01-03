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
### 03.2.1 Linux文件属性
* 用ls -al 文件名查看（包括隐藏文件）：
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

* 注意：这个文件容量是以byte为单位的，如果想要文件自适应大小，则可以用 ls -al -h 文件名这个命令。
```
[root@i-jjr0xl1a jun]# ls -al a.txt
-rw-r--r-- 1 root root 4113 Dec 29 15:46 a.txt
[root@i-jjr0xl1a jun]# ls -al -h a.txt
-rw-r--r-- 1 root root 4.1K Dec 29 15:46 a.txt
```

| 权限 | 连结 | 拥有者 | 群组 | 文件容量 | 修改日期 | 档名|
|:-- |:-- |:-- |:-- |:-- |:-- |:-- |
| -rw------- | 1 |root|root|1345|Dec 29 14:42|.bash_history|

* 文件属性的示意图如下:

  ![文件属性的示意图](03-图片/文件属性的示意图.png)

#### 第一栏：代表这个文件的类型和权限

 ![文件类型与权限的内容](03-图片/文件类型与权限的内容.png)



* 第一个字符代表这个文件是目录、文件或链接文件等等。

| 简写 | 含义 | 举例 |
|:-- |:-- |:-- |
| d | 目录 |dr-xr-xr-x. 18 root root 4096 Dec 29 14:15 ..|
| - | 文件 |-rw-------   1 root root 1345 Dec 29 14:42 .bash_history|
| l | 连结档（link file） | 暂无例子 |
| b | 装置文件里面的可供储存的接口设备（可随机存取装置） | 暂无例子 |
| c | 装置文件里面的串行端口设备（如鼠标、键盘） | 暂无例子 |

* 接下来的三个为一组，且均为 **rwx** 三个参数的组合
 * 第一组为文件拥有者可具备的权限
 * 第二组为加入此群组的账号的权限
 * 第三组为非本人且没有加入本组之其他账号的权限

| 参数 | 含义 |
|:-- |:-- |
| r | read（读） |
| w | write（写）|
| x | execute（执行）|
* r：read（读）；w：write（写）；x：execute（执行）

#### 第二栏：表示有多少档名连结到次节点
* 每个文件都会将它的权限与属性记录到文件系统的 i-node 中，们使用的目录树却是使用文件名来记录，因此每个档名会连结一个 i-node 号。
* 这个属性记录的就是有多少不同的档名连结到同一个 inode 号码

#### 第三栏：这个文件（或目录）的拥有着账号
#### 第四栏：这个文件的所属群组
#### 第五栏：这个文件容量的大小
* 默认单位byte
* 如果要让文件自适应，则ls -al -h

#### 第六栏：这个文件的建档日期或者是最近修改的日期
* 如果这个文件被修改的时间距离现在太久了，那么时间部分仅会显示年份而已。
* 如果想要显示完整的时间格式：ls -al -full-time

#### 第七栏： 这个文件的档名
* 如果档名之前多了一个 **.**，则代表这个文件为隐藏文件

## 03.2.2 如何改变文件属性与权限
* chgrp：改变文件所属群组
* chown：改变文件拥有着
* chmod：改变文件的权限，SUID,SGID,SUIT等等的特性

### chgrp：改变所属群组
* chgrp = change group
* 语法： chgrp [-R] group dirname/filename
```
 -R：进行递归（recursive）的持续更变，
     亦即连同次目录下的所有文件、目录都更新成为这个群组之意。
     常常用在变更某一目录内所有文件之情况。
```
* 前提：要被改变的组名必须要在 /etc/group 文件内存在才行哦~
* 例1：将/home下的b.txt修改到testing组（不存在），
```
[root@i-jjr0xl1a /]# chgrp testing /home/b.txt
chgrp: invalid group: ‘testing’
```
* 例2：将/home下的b.txt修改到jun组（存在）
```
[root@i-jjr0xl1a /]# chgrp jun /home/b.txt
[root@i-jjr0xl1a /]# ls -al -h /home/b.txt
-rw-r--r-- 1 root jun 0 Dec 29 17:38 /home/b.txt
```

### chown：改变文件拥有者
* chown = change owner
* 语法：
  * chown [-R] 账号名称 文件或目录  
  * chown [-R] 账号名称：组名 文件或目录(目录下的所有次目录或文件同时更改文件拥有者)
```
更改文件的所有者：
[root@i-jjr0xl1a jun]# ls -al a.txt
-rw-r--r-- 1 jun root 17 Jan  1 23:18 a.txt
[root@i-jjr0xl1a jun]# chown root a.txt
[root@i-jjr0xl1a jun]# ls -al a.txt
-rw-r--r-- 1 root root 17 Jan  1 23:18 a.txt  
```
```
递归更改目录及目录下的的文件所有者：
[root@i-jjr0xl1a jun]# ls -dl luna
drwxr-xr-x 2 root root 4096 Jan  2 18:28 luna
[root@i-jjr0xl1a jun]# chown -R jun luna
[root@i-jjr0xl1a jun]# ls -dl luna
drwxr-xr-x 2 jun root 4096 Jan  2 18:28 luna
[root@i-jjr0xl1a jun]# cd luna
[root@i-jjr0xl1a luna]# ls -al
total 8
drwxr-xr-x 2 jun root 4096 Jan  2 18:28 .
-rw-r--r-- 1 jun root    0 Jan  2 18:28 1.txt
-rw-r--r-- 1 jun root    0 Jan  2 18:28 2.txt
```

### 问题：什么时候使用chgrp或chown？
  * 最常见的就是在复制文件给你之外的其他人的时候
  * 用cp指令来说明：
    * 语法： cp 来源文件 目标文件
  * 例如：将/home/jun下面的b.txt复制给warm用户，但是warm用户无法修改，所以需要将这个文件的拥有者和群组修改一下~
```
[jun@ali2 ~]$ cp b.txt b1.txt
[jun@ali2 ~]$ ls -al b1.txt*
-rw-rw-r-- 1 jun jun 659 Jan  3 14:13 b1.txt
```

### chmod：改变权限
* 权限的设定有两种方法：使用文字或符号来进行权限的变更

#### 数字型改变文件权限
* 权限字符对应的数字

| 权限字符 | 数字 |
|:-- |:-- |
| r | 4 |
| w | 2 |
| x | 1 |

* 每种身份（owner/group/others）各自的权限（r/w/x）分数是需要累加的。
  * 例：当权限位[-rwxrwx---]分数则是
  ```
  owner = rwx = 4+2+1 = 7
  group = rwx = 4+2+1 = 7
  others = --- = 0+0+0 = 0
  ```
  所以设定权限的变更时，该文件的权限数字就是770啦~

* 数字型改变权限语法：chmod [-R] xyz 文件或目录
  * xyz：数字类型的权限属性，为rwx属性数值的相加
  * -R： 进行递归的持续变更

#### 符号类型改变文件权限
* 符号类型改变权限语法

| 命令 | 对象 | 权限增减 | 权限 | 对象 |
|:-- |:-- |:-- |:-- |:-- |
| chmod | u/g/o/a(=all) | +/-/= | r/w/x | 文件或目录 |


## 03.3 目录与文件之权限意义
### 权限对文件的重要性
* r(read)： 可读取此一文件的内容，如读取文本文件的文字内容等
* w(write)： 可以编辑、新增或是修改该文件的内容（但不含删除文件）
* x(eXecute): 该文件具有可以被系统执行的权限

### 权限对目录的重要性
* r：表示具有读取目录结构列表的权限，当具有r权限时，表示你可以查询该目录下的文件名数据。可以利用ls命令将该目录的内容显示出来哦~
* w：表示具有异动该目录结构列表的权限，即下面的权限：
  * 建立新的文件与目录
  * 删除已经存在的文件与目录（且不论该文件的权限为何！）
  * 将已存在的文件或目录进行更名
  * 搬移该目录内的文件、目录位置
* x：代表用户能否进入该目录成为工作目录（变换目录的指令cd）
### 小结

| 组件 | 内容 | 迭代物件 | r | w | x |
|:-- |:-- |:-- |:-- |:-- |:-- |
| 文件 | 详细资料data | 文件文件夹 | 读到文件内容 | 修改文件内容 | 执行文件内容 |
| 目录 | 档名 | 可分类抽屉 | 读到档名 | 修改档名 | 进入该目录的权限（key） |
* 工作目录对于指令的执行是非常重要的，如果你在某目录下不具有x权限，那么就无法切换到该目录下，也就无法执行该目录下的任何指令，即使你具有该目录的r和w权限
*
