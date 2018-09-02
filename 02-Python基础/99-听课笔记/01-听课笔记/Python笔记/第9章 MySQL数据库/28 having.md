### having过滤

having 在分组之后进行过滤
where 在分组之前进行过滤
区别:
select post,group_concat(name),count(id) from employee group by post
select post,group_concat(name),count(id) from employee group by post having count(id)<2;
