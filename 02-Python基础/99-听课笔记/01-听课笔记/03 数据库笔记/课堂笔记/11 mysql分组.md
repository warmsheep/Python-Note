## mysql分组
* group by
select count(part_id),max(id) from userinfo5 group by part_id;

count
max
min
sum
avg

select count(part_id),count(id),max(id) from userinfo5 group by part_id;错误

select part_id from userinfo5 where count(id)>10 group by part_id;错误

如果对于聚合函数结果进行如此筛选时？必须使用having
select part_id,count(id) as num from userinfo5 group by part_id having count(id)>10 ;
where能加但是不能加上聚合函数结果。
