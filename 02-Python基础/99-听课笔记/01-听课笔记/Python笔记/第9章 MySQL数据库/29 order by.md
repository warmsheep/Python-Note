### order by

升序排列

select * from employee order by age asc;

降序排列
select * from employee order by age dsc;
select * from employee order by asc,id dsc;
先按照age升序排列，如果age相同，按照ID降序排

having --distinct--order by--select

limit



select * from employee;


没有分组就不能where聚合函数
分组后才能用聚合函数
