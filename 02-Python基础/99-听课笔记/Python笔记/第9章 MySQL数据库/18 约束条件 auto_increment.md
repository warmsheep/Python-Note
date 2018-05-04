### auto_increment

create table t20(
  id int auto_increment,
  name char(6)
  );

```
ERROR 1075 (42000): Incorrect table definition; there can be only one auto column and it must be defined as a key
```
create table t20(
  id int primary key auto_increment,
  name char(6)
  );
desc t20;

```
+-------+---------+------+-----+---------+----------------+
| Field | Type    | Null | Key | Default | Extra          |
+-------+---------+------+-----+---------+----------------+
| id    | int(11) | NO   | PRI | NULL    | auto_increment |
| name  | char(6) | YES  |     | NULL    |                |
+-------+---------+------+-----+---------+----------------+
```

可以只传入name，不用传入id，id自动增长

insert into t20(name) values ("egon"),("alex");

select * from t20;


+----+--------+
| id | name   |
+----+--------+
|  1 | egon   |
|  2 | alex   |
+----+--------+


insert into t20(id,name) values (7,"jssies");

insert into t20(name) values ("egon1");
select * from t20;

| id | name   |
+----+--------+
|  1 | egon   |
|  2 | alex   |
|  7 | jssies |
|  8 | egon1  |
+----+--------+


show variables like "auto_inc%";

+--------------------------+-------+
| Variable_name            | Value |
+--------------------------+-------+
| auto_increment_increment | 1     |
| auto_increment_offset    | 1     |
+--------------------------+-------+

auto_increment_increment:步长，默认为1
auto_increment_offset：起始偏移量，默认为1

设置步长:

set session auto_increment_increment=5;

设置全局的步长
set global auto_increment_increment=5;
设置好了需要退出，重新进来


设置偏移量

set session auto_increment_offset=5;
强调:起始偏移量小于等于步长，否则失效。

create table t21(
  id int primary key auto_increment,
  name char(16)
  );

insert into t21(name) values ("egon"),("alex"),("wxx");


清空表
delete from t20;

show create table t20;
发现他的自增长并没有变为1，还是和之前一样的，重新插入，会从之前的表中开始计数。


所以一般不用delete,一般用trancate

truncate t20;
