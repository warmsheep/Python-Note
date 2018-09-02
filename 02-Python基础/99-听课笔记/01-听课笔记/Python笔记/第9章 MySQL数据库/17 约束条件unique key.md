### unique key

唯一的值


create table department(
  id int,
  name char(10)
  );

insert into department values(1,"IT");
insert into department values(2,"IT");

 drop table department;


##### 单列唯一
 create table department(
   id int unique,
   name char(10) unique
   );

 insert into department values(1,"IT");
 insert into department values(2,"IT");

```
 ERROR 1062 (23000): Duplicate entry 'IT        ' for key 'name'
```

drop table department;



方式二
create table department(
  id int,
  name char(10),
  unique(id),
  unique(name)
  );

##### 联合唯一
字段1+字段2 唯一

create table services(
  id int unique,
  ip char(15),
  port int,
  unique(ip,port)
  );

insert into services values(1,"192.168.11.10",80),(2,"192.168.11.10",81),(3,"192.168.11.10",82);

 
