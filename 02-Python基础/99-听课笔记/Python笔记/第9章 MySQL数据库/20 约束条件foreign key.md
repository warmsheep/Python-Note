### foreign Key

用来建立表之间的关系

先建被关联的表，并保证被关联的字段唯一，再建关联的表
必须保证id唯一性，unique或者primary key

建立表关系


create table dep(
  id int primary key,
  name char(16),
  comment char(50)
  );


create table emp(
  id int primary key,
  name char(10),
  sex enum("male","female") not null default "male",
  dept_id int,
  foreign key(dept_id) references dep(id)
  on delete cascade
  on update cascade
  );

on update cascade 更新同步
on delete cascade 删除同步

desc emp;

插入数据
先往被关联表插入记录，再往关联表插入。

insert into dep values (1,"IT","技术能力有限部门"),(2,"销售","销售能力不足"),(3,"财务","花钱最多");



insert into emp values (1,"egon","male","1");
insert into emp values (2,"alex","male","1"),(3,"wxx","female","2"),(4,"jinxx","female","3");

delete from emp where dept_id=1;
delete from dep where id=1;


直接先删除dep
delete from dep where id =2;

ERROR 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails (`db4`.`emp`, CONSTRAINT `emp_ibfk_1` FOREIGN KEY (`dept_id`) REFERENCES `dep` (`id`))

因为有关联关系，不能随便删除

update dep set id =333 where id =3;
也会出现错误
