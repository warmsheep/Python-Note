## mysql操作补充
增
  insert into tb(name,age) values("alex",12)
  insert into tb(name,age) values("alex",12),('root',18);
  create table tb11(
      id int auto_increment primary key,
      name varchar(32),
      age int
    )engine=innodb default charset=utf-8;

    create table tb12(
        id int auto_increment primary key,
        name varchar(32),
        age int
      )engine=innodb default charset=utf-8;
      如何把tb11的表插入到tb12中？
      insert into tb12(name,age) select name,age from tb11;
删
  delete from tb12;
  delete from tb12 where id !=2;
  delete from tb12 where id =2;
  delete from tb12 where id >2;
  delete from tb12 where id>=2;
  delete from tb12; id>=2 or name='alex';

改
  update tb12 set name='alex',age=19 where id>12 and name="xx";
查
  select * from tb12;
  select id,name from tb12;
  select id,name from tb12 where id>2;
  select name as cname,age from tb12;
  select name as cname,age,1 from tb12;

其他:
select * from tb where id!=1;
select * from tb12 where id in (1,5,12);
select * from tb12 where id not in (1,5,12);
select 8 from tb12 where id in between 1 and 201;(闭区间)
select * from tb12 where id in (select id from tb11)


以a开头:
a%
以a结尾
%a
ab
abc
包含a:
%a%
select * from tb12 where name like "a%"

### 分页
取前10个:
select * from tb12 limit 10;
select * from tb12 limit 1,1;(起始值，后面取几条)
select * from tb12 limit 0,10;取前10条
select* from tb12 limit 10 offset 20;取10-20条


page=input("输入要查看的页码")
page = int(page)
(page-1) * 10
select * from tb12 limit 0,10;1
select * from tb12 limit 10,10;2

* 排序
select * from tb12 order by id desc;降序
select * from tb12 order by id asc;升序
select * from tb12 order by id desc,age desc;
