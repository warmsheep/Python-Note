group by
在where 后面运行，写查询语句也是写在where之后
selectn * from employee group by post
每个组的第一条记录

设置严格格式
set global sql_mode="ONLY_FULL_GROUP_BY";
代表:只能取分组的字段，以及每个组聚合结果
select post from employee group by post

聚合函数
max
min
avg
sum
count

查每个职位都有多少个员工
select count(id)  as emp_count from employee group by post

强调:一定不要用unique字段用作分组依据，没有意义。
没有group by则整体默认算做一组
select max(salary) from employee

grop_concat

select post,group_concat(name) from employee group by post;

select post,group_concat(name) from group by post;
