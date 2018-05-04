* 操作文件夹（库）

增
create database db1 charset utf8;


查
show create database db1;查看刚刚新建的数据库
show databases;查看所有数据库

改

alter database db1 charset gbk;
删
drop database db1;


* 操作文件（表）
切换文件夹
use 数据库名;

查看当前所在的文件夹

```
select database();
```

增

```
create table t1(id int,name char)
字段 字段类型
```
查

```
show create table t1;
show tables;查看所有的表
desc t1;
```

改

```
alert table t1 modify name char(6);
alert table t1 change name NAME char(7);
```

删

```
drop table t1
```

* 操作文件内容（记录）

增

```
insert t1(id,name).values(1,"egon1";2,"egon2";3,"egon3")
```

查
```
select id,name from db1.t1
select * from db1.t1
```

改
```
update db1.t1 set name="SB"
```
删
```
delete from db1.t1;
delete from db1.t1 where id=2
```
