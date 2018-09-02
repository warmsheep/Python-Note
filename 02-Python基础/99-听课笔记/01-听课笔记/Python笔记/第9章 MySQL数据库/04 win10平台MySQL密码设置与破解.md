
* 查看默认账号

```
mysql> select user();
user()
ODBC@localhost
```
ODBC:本地账号

* 切换其他账号

```
mysql -u指定账号(不用空格) -p(指定密码)
```

```
mysql  -uroot -p
```

```
mysql> select user();
user()
root@localhost
```
root账号就是MySQL里的管理管理员账号

* 给root账号设置密码

```
mysqladmin -u指定用于 -p原始密码 password"新密码"
```
会警告，因为修改的密码是明文的

修改之后不输入密码再登录会报错

```
mysql -uroot -p
```

* 还想修改密码

```
mysqladmin -u指定用于 -p原始密码 password"新密码"
```

* 如果忘记了mysql账号的密码

账号密码文件存放在mysql\\data\\mysql这里面的表放账号密码

开启mysql服务

net start MySQL

关闭mysql服务

net stop MySQL


1、不加载这里的文件

```
mysqld --skip-grant-tables
```
但是这样默认的是ODBC账号


```
mysql -uroot -p
```

用root账户来更改账户密码

```
update mysql.user set password=password("新密码") where user="指定账户" and host="localhost"(说明这是本地账号)

flush privileges(刷新一下授权表，也就是更新密码)
```


```
tasklist |findstr mysql
taskkill /F /PID 进程号
```

服务端的ip端口
ip:127.0.0.1
端口:3306
```
mysql -uroot -p123 -h 127.0.0.1 -P 3306
```


```
```
