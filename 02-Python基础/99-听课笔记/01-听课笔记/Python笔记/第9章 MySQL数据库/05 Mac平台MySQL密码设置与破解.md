
mysql

```
select user();
user()
root@localhost
```



* 修改密码

在linux平台下听

原始密码不需要加""，输入下面命令后再输入原始密码

```
mysqladmin -uroot -p原始密码 password "新密码"
```

* 登录

```
mysql -uroot -p
```

* 无需密码启动

```
mysqld_safe --skip-grant-tables
```

* 然后在登录
```
```

* 然后修改密码

```
update mysql.user set password=password("") where user="root" and host="localhost"
flush privileges
```

```
ps aux | grep mysql
kill -9
```
```
```
```
```
