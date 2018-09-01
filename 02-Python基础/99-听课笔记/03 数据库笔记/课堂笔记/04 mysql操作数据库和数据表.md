## mysql操作数据库&数据表
### 操作文件夹(数据库没有修改)
create databases db2 default charset utf8;
show databases;
drop database db1;



### 操作文件
show tables;
create table t1(id int,name char(10),) default charset=utf8;
select * from t1;
* 新建表
create table t1(
    列名 类名 null,
    列名 类名 not null,
    列名 类名 not null default 1,
    列名 类名 auto_increment primary key,
    id int,
    name char(10),
) engine=innodb default charset=utf8;

auto_increment:自增 一个表中只能有一个自增列
primary key:表示 约束(不能重复且不能为空);加速查找
auto_increment必须和primary key连用
* 清空表
  delete from t1;把内容删掉，但是自增id会根据之前的数字开始
  truncate table t1;把自增id也会清空
* 删除表:
  drop table t1;

```
编码的问题:在新建文件夹的时候设置编码，在新建表格中也设置编码
引擎:
innodb:支持事物
create table t1(id int,name char(10),) engine=innodb default charset=utf8;
myisam:不支持，数据会丢失
```

### 操作文件的内容
插入数据
insert into t1(id,name) values(1,'egon');

查看数据
select * from t1;
