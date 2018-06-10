## mysql连表

select * from userinfo5,department5 where userinfo5.part_id=department5.id;


select * from userinfo5 left join department5 on userinfo5.part_id=department5.id;

select * from userinfo5 right join department5 on userinfo5.part_id=department5.id;

select * from userinfo5 inner join department5 on userinfo5.part_id=department5.id;

左右区别:
左边会全部显示

右边会全部显示

连表的时候如果列名重复，可以加上表名

inner join:
只要有null的值就会全部隐藏掉
