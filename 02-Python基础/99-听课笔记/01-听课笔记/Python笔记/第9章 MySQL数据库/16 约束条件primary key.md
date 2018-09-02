### primary key

约束:not null unique
存储引擎：innodb 对于innodb存储引擎来说，一张表内必须有一个主键

查看数据库
show create table t14;


##### 单列主键

create table t17(
  id int primary key,
  name char(16)
  );

desc t17;

```
+-------+----------+------+-----+---------+-------+
| Field | Type     | Null | Key | Default | Extra |
+-------+----------+------+-----+---------+-------+
| id    | int(11)  | NO   | PRI | NULL    |       |
| name  | char(16) | YES  |     | NULL    |       |
+-------+----------+------+-----+---------+-------+
```

insert into t17 values(1,"egon"),(2,"alex");

insert into t17 values(2,"wxx");

```
ERROR 1062 (23000): Duplicate entry '2' for key 'PRIMARY'
```

insert into t17(name) values ("wxx");

select * from t17;

+----+------------------+
| id | name             |
+----+------------------+
|  0 | wxx              |
|  1 | egon             |
|  2 | alex             |
+----+------------------+



create table t18(
  id int not null unique,
  name char(15)
  );

desc t18;


##### 复合主键

create table t19(
  ip char(15),
  port int,
  primary key(ip,port)
  );


insert into t19 values ("1.1.1.1",80);
