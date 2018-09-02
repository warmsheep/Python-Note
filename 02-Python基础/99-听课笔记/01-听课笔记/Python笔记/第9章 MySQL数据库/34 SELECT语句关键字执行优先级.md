
desc department;

查询平均年龄大于30岁的部门名

```
select department.name,avg(age) from employee inner join department on employee.dep_id=department_id
group by department.name
having avg(age)>30;
```
