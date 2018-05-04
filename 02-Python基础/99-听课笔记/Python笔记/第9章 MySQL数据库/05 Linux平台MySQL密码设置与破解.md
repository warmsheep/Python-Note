* 查看默认用户

```
select user();
user()
root@localhost
```

* 设置密码

```
mysqladmin -uroot -p原始密码 password "新密码"
```

* 先干掉mysql

```
systemctl stop mariadb
```

* 无密码启动mysql
服务端
```
mysqld_safe --skip-grant-tables
```

客户端
```
mysql -uroot -p
```


```
update mysql.user set password=password("") where user="root" and host="localhost"
flush privileges;
```

* 杀死mysql

```
pkill -9 mysql
```

* 再启动

```
systemctl start mariadb
```


```
```


```
```


```
```


```
```
