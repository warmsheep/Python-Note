## 1. mysql视图
某个查询语句设置别名，日后方便使用，虚拟的
create view v1 as select * from student where sid>10;

视图能插入数据吗？不能
原始表中插入的数据会在视图中展示吗？会

创建视图
create view 视图名称 as sql语句
PS:视图是虚拟的
修改视图
alter view 视图名称 as sql语句
删除
drop view 视图名称
不推荐使用
## 2. 触发器
当对某张表做；增删改操作时，可以使用触发器自定义关联行为。
不推荐使用
insert into tb(...)
插入前
create trigger 触发器名字 before  insert on tb1 for each row
begin
  insert into tb2
end

插入后
create trigger 触发器名字 after  insert on tb1 for each row
begin
  insert into tb2
end

删除前
create trigger 触发器名字 before  delete on tb1 for each row
begin
  insert into tb2
end

删除后
create trigger 触发器名字 after delete on tb1 for each row
begin
  insert into tb2
end

更新前
create trigger 触发器名字 before update on tb1 for each row
begin
  insert into tb2
end

更新后
create trigger 触发器名字 after update on tb1 for each row
begin
  insert into tb2
end


delimiter //

创建触发器
delimiter //
create trigger t1 before  insert on tb1 for each row
begin
  insert into tb2(name) values('sasd')
end //
delimiter;

一次插两条的话呢？也会新增两条，因为是each row



NEW:新数据
OLD:老数据

插入新的数据
delimiter //
create trigger t1 before  insert on tb1 for each row
begin
  insert into tb2(name) values(NEW.sname)
end //
delimiter;

delete：有old
delimiter //
create trigger t1 before delete on tb1 for each row
begin
  insert into tb2(name) values(NEW.sname)
end //
delimiter;

update既有老的又有新的

## mysql函数

def f1():
  pass
f1()
bin()
内置函数:
  select curdate();(去博客看)
  select char_length();
  时间格式
  curdate()

  执行函数: select curdate();
  blog
  id title ctime
  1 asdf 2019-11-11 11:11
  2 adsa 2019-11-10 11:20
  如何按月分组:
  select (ctime),count(id) from blog group date_format(ctime,"%Y-%m");


自定义函数:
也可以进行调用
delimiter \\
create function f1(
  i1 int,
  i2 int
  )
return int
begin
  declare num int;
  set num = i1 + i2
  return (num)
end \\
delimiter;

select f1(1,100);

函数有返回值，函数中不能写select * from tb；
但是存储过程可以写。

## 存储过程(没有返回值)
保存在mysql上的一个别名 =>一坨sql语句
别名()
用来替代程序员写sql语句
加括号是为了预留位置传参数。
1.简单存储过程
delimiter \\
create procedure p1()
begin
  select * from student;
  insert into teacher(tname) values("ct");
end \\
delimiter ;

call p1();

pymysql如何调用存储过程

cursor.callproc("p1")
cursor.fetchall()
cursor.commit()
2.传参数(in,out,inout)
delimiter \\
create procedure p1(
  in n1 int,
  in n2 int
)
begin
  select * from student where sid > n1;
end \\
delimiter ;

call p2(12,3);

cursor.proc('p2',(12,2))

3 如何有返回值 参数out

delimiter \\
create procedure p2(
  in n1 int,
  out n2 int
)
begin
  set n2 = 123123;
  select * from student where sid > n1;
end \\
delimiter ;
set @v1 = 0;--创建了一个session变量为v1；
call p2(12,@v1)
select @v1 --123123

set @_p2_0 = 12
set @_p2_1 = 2
call p2(@_p2_0,@\_p2_1)
select @_p2_0,@\_p2_1



delimiter \\
create procedure p3(
  in n1 int,
  out n2 int
)
begin
  set n2 = 123123;
  select * from student where sid > n1;
end \\
delimiter ;

set @v1 = 0;
call p3(12,@v1)--结果集
select @v1;--返回值

pymysql调用
cursor.proc('p3',(12,2))--只能拿到结果，不能
s1 = cursor.fetchall()
拿到返回值
要想拿到返回值，必须再进行一次查询

cursor.execute('select @_p3_0,@\_p3_1');


inout:能传入也能取回来

看公司情况一般用不用存储过程
方式一:
  mysql:存储过程
  程序:调用存储过程
方式二:
  mysql：。。。
  程序:sql语句
方式三:
  mysql:...
  程序:类和对象(sql语句)

特性:
1.能传参数 in  out inout
2.pymysql

为什么有结果集又有out造的返回值？
out用户标识存储过程的执行结果

4.事务

delimiter \\
create procedure p4(
  out status int
  )
begin
  1.声明如果出现异常则执行{
    set status = 1;
    rollback;
  }
  开始事务
    -- A账户减去100
    -- B账户加上90
    -- C账户加上10
    commit()
  结束
  set status = 2;
end \\
delimiter ;

5.游标
循环添加值
=== 游标
1.声明游标
2.获取A表中数据
  mycursor select id,num from A
3.for row_id,row_num in mycursor:
      #检测循环是否还有数据，如果无数据break
      insert into B(num) valuse (row_id+row_num)

delimiter \\
create procedure p6()
begin
    declare row_id int;--自定义变量1
    declare row_num int;--自定义变量2
    declare done int default false;
    declare temp int;

    declare my_cursor cursor for select id,num form A;
    declare continue handler for not found set done = true;

    open my_cursor;
        xxoo:loop
            fetch my_cursor into row_id,row_num;
            if done then
                leave xxoo;
            end if;
            set temp = row_id + row_num;
            insert into B(num) values(temp);
        end loop xxoo;
    close my_cursor;
delimiter ;

call p6();

6.动态执行sql(防sql注入)
delimiter //
create procedure p7(
  in tpl varchar(255),
  in arg int,
  )
begin
    1.预检测某个东西 SQL语句的合法性
    2.格式化 sql = tpl + arg
    3.执行sql语句
end//
delimiter ;

call p7('select * from tb where id > ?',9)
====> 动态执行sql


delimiter //
create procedure p8(
  in nid int,
  )
begin
    set @nid = nid;
    prepare pro from "select * from tb where id > ?";
    execute xxx using @nid;--格式化后面的值只能是session的变量
    deallocate prepare prod;
end//
delimiter ;

数据库相关操作
  1.sql语句
    - select xx() from xxx;
    先找找有没有函数(字符串的操作、时间操作)
    - 函数不能加速查找，一般用索引加速查找，对性能要求高，就不要用函数
  2.利用mysql内部提供的功能
作业:
一、sql题目
二、创建数据库
   表: id  name email gender
    插入三百万行数据
    预习索引 orm操作:sqlAlchmy
内容回顾:
    1.数据库是什么
    2.MySQL安装
    3.用户授权
    4.数据库操作
      数据表操作
          外键
            - 一对多
            - 多对多
            - 一对一
          数据类型
          自增
          唯一索引
            - unique
          主键
          连表:left/right/inner join
          组合:union union all(不去重)
      数据行操作
          排序:order by desc/asc
          分组:group by
          筛选:where having
      pymysql
        - 连接 connect(...)
        - 操作(游标)
          - 增删改 commit
          - 查 fetchone fetchall offset
        - sql注入

        - 存储过程调用方式
          - call()
          - select @_存储过程名称_0
        - commit
        - select fetchone
        - sql注入(注释用 -- 后面的语句不生效)
            select * from user where username = "'x'or 1=1 --" and pwd = 'sfd';

      临时表:
      通配符
      5.视图
          - 临时表(虚拟的)
      	触发器
          - 针对没一行数据
        函数
          - 调用select 函数(参数)
        存储过程
          - in out inout
          - 游标
          - 事物(多个数据库操作当做一个整体，全部成功才能提交，否则回滚)


        分页:limit
        
## 索引
作用:
  - 约束
  - 加速查找

索引:

  - 普通索引:加速查找
  - 主键索引:加锁查找 + 不能为空 + 唯一
  - 唯一索引:加速查找 + 不能重复
  - 联合索引(多列):
    - 联合主键索引
    - 联合唯一索引
    - 联合普通索引

加速查找:
  快:
    select * from tb where name = 'asdf';
    select * from tb where id = 999;
  假设:
    id name email
    ...
    无索引:从前到后一次查找
      索引:
         id 创建额外的文件(某种格式存储)
         name 创建额外的文件(某种格式存储)
         name email 创建额外的文件(某种格式存储)
创建索引:
create index ix_name on userinfo3(email);

索引种类:
  hash索引:索引表，hash表中的值和存的值的顺序是不一样的,单值快，范围查找不行

  btree索引:
    二叉树
    结果:快

建立索引:
  - a. 额外的文件保存特殊的数据结构
  - b. 查询快，插入更新删除慢
  - c. 命中索引
    select * from userinfo3 where email="asdf";
    select * from userinfo3 where email like "asdf";--这样无法命中索引
创建普通索引:
create index 索引名称 on 表名(列名);
drop index 索引名称 on 表名;

唯一索引:
create unique index 索引名称 on 表名(列名);
drop unique index 索引名称 on 表名;

联合索引:
create unique index 索引名称 on 表名(列名,列名);

覆盖索引:
select id from userinfo3 where email = 'sf';
- 在索引文件中直接获取数据，不是真实的索引，只是一个名词

索引合并:
- 多个单列索引合并使用
select * from userinfo3 where email = 'sf' and id='999';

- 组合索引
create index ix_name_email on userinfo3(name,email,exc)
最左前缀匹配
    select * from userinfo3 where name = 'alex';
    select * from userinfo3 where name = 'alex' and email = 'asd';
    select * from userinfo3 where email = 'asd';-- 这样是不会走索引的

组合索引效率 > 索引合并

全文索引

2.频繁查找的列创建索引
  - 创建索引
  - 命中索引

使用用户量少
  title like '%雷电%'
第三方工具
  城镇化 增长率 省份 1，21，31
  select * from tb where id in (1,21,31)
避免使用函数:
  select * from userinfo3 where reverse(email) = 'alex23@qq.com'
  在python中直接反转了，然后再去查

select * from userinfo3 where id = 999 or name = 'alex12' -- id是索引但是name不是索引，导致无法命中索引，查询效率降低。

select * from userinfo3 where id = 999 or name = 'alex12' and email = 'alex' --email和id都是索引，这种情况会忽略name

非主键索引如果类型不一致就会出现查询效率降低
select * from tb where age = 12;
select * from tb where age = '12';

!=特别的如果是主键，则还是会走索引:
select * from tb name ！= "alex";

\>:特别的如果是主键或索引是整数，则还是会走索引
如果是文字，则不走索引

select * from tb name > 'alex';



order by当根据索引排序的时候，选择的映射如果不是索引，则不走索引
特别的，如果对主键排序，则还是走索引；
select * from tb1 order by nid;

## 索引注意事项
- 避免使用select *
- count(1)或count(列)代替count(\*)
- 创建表时尽量用char代替varchar
- 标的字段顺序固定长度的字段优先
- 组合索引代替多个单列索引(经常使用多个条件查询时)
- 尽量使用短索引

    create index ixxx on tb(title);
    如果是text类型，是不能直接建立索引的

- 使用连接(join)来代替子查询(sub-queries)
- 连表时注意条件类型需一致
- 索引散列值(重复少)不适合索引，例:性别不合适


## mysql执行计划介绍
执行计划：让mysql预估执行操作
慢
explain select * from userinfo3;
type: all(全表扫描)
快
explain select * from userinfo3 where email = 'alex';
type: ref(走索引)
type: const(走索引)

## DBA工作
慢日志:
  执行时间 > 10
  未命中索引
  日志文件路径
配置:
  内存:show variables like "%query%";
    set global slow_query_log = on;
    set global 变量名 = 值;
  配置文件
    mysqld --default-file='D:\\my.conf'
  my.conf内容:
    slow_query_log = on;
    slow_query_log_file = D:\\


my-default.ini;
是安装的时候就有配置文件
port = 3306默认
如果把这个文件放在另外地方，启动的时候就需要加上文件路径
mysqld --default-file='E:\\\\'
注意：修改配置文件之后，需要重启服务



## mysql分页性能相关方案
select * from userinfo3 limit 0,10;
select * from userinfo3 limit 10,10;
select * from userinfo3 limit 20,10;

翻页越大越慢，仅仅这样写不行的
解决方案:
  - 不让看
  - 索引表中扫描
  select * from userinfo3 where id in (select id from userinfo3 limit 20000,10);--运行也不会很快，因为还是要扫描20000条
  - 方案:
        - select * from userinfo3 where id > 200000 limit 10;
        - select * from userinfo3 where id < 2000021 order by desc imit 10;
    - 记录当前页面看见的最大id或最小id
        - 不要认为id是连续的，所以无法直接使用id范围查找
        1.页面只有上一页，下一页
          max_id,min_id
          select * from userinfo3 where id > max_id limit 10;
          select * from userinfo3 where id < min_id order by desc limit 10;
        2.上一页 192 193 【196】 197 198 199 下一页
        如果跨页的话，中间的数据全部都要拿到
          select * from (select * from userinfo3 desc where id > max_id limit 30) as N order by N.id limit 10;



## 面向对象回顾
无面向对象，完全可以编程
    def func(arg):
        return arg + 1
1.提取共性
2.分类
3.模板约束
  一类事物共同具有:属性和行为
  class Person:
    def __init__(self,name):
        self.name = name
4.当一类函数共用同样参数时候，可以转变成类进行--分类
  面向对象:数据和逻辑组合在一起
    函数编程:数据和逻辑分离

特殊方法
  1. init
  2. __call__
  3. __getitem__
  4. __setitem__
  5. __delitem__

## 自己开发web框架
- socket
- http协议(请求头和请求体中间用两个换行分开的)
- HTML知识
- 数据库(pymysql,sqlAlchmy)


## ORM:SQLAlchmy 关系对象映射
- 用类和对象对数据库操作
- 作用
  - 1.提供简单的规则
  - 2.自动转换成SQL语句

- DB first:手动创建数据库以及表->ORM框架->自动生成类
- code first:手动创建类 -> ORM框架 -> 以及表

- 功能:
  - 创建数据库
    - 连接数据库(非sqlalchemy做的，是pymysql做的)
    - 类转换sql语句(sqlalchemy只做这件事儿)
    - max_overflow最大连接数(sqlAlchmy完成的)
  - 操作数据行
    - 增
    - 删
    - 改
    - 查

先装pymysql或者mysqldb，然后再用sqlalchemy

创建单表

class UserType(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key = True,auto_increment=True)
    title = Column(String(32),nullable = True,index = True)

class Uers(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True, auto_increment = True)
    name = Column(String(32), nullable = True, index = True)
    extra = Column(String(16), unique = True)
    user_type_id = Column(Integer,Foreignkey('usertype.id'))

    __table_args__ = (
        UniqueConstraint("id","name"),
        Index("ix_n_ex","name","extra")
      )
    def create_db():
        engine = create_engine("mysql+pymysql://root:@127.00.1:3306/s4day62db?charset=utf8", max_overflow = 5)
        Base.metadata.create_all(engine)
    def drop_db():
        pass

engine = create_engine("mysql+pymysql://root:@127.00.1:3306/s4day62db?charset=utf8", max_overflow = 5)
Base.metadata.create_all(engine) 创建
Base.metadata.drop_all(engine) 删除
#类--》表
#对象--》行
#增加
Session = sessionmaker(bind=engine)
session = Session()
obj1 = UserType(title='普通用户')
session.add(obj1)#转换成sql语句
增加多行
objs = [
  UserType(title="s1"),
  UserType(title="s2"),
  UserType(title="s3"),
  UserType(title="s4"),
  UserType(title="s5"),
  UserType(title="s6"),
]
session.add_all(objs)
session.commit()
session.close()
## 查
user_type_list = session.query(UserType).all()#是一个list，list里面是每一个对象
for row in user_type_list:
    print(row.id,row.title)


user_type_list = session.query(UserType.id,UserType.title).filter(UserType.id > 2)#条件查询filter

## 删除
先查再删
session.query(UserType.id,UserType.title).filter(UserType.id > 2).delete()#条件查询filter再删除

## 修改
session.query(UserType.id,UserType.title).filter(UserType.id > 0).update({"title":'黑金'})#条件查询filter再修改
session.query(UserType.id,UserType.title).filter(UserType.id > 0).update({UserType.title:UserType.title+'x'},synchronize_session = False)

session.query(UserType.id,UserType.title).filter(UserType.id > 0).update({UserType.num:UserType.num+1},synchronize_session = "evaluate")

## 分组
## 排序
## 连表
## 通配符
## limit
## having
## union
## join
## 原生sql

filter_by(参数)
filter(表达式)

## 子查询

## 便利的功能
sql作为映射放在这里

session.query(UserType,session.query(Users).filter(Users.id == 1).subquery())
这样还是迪笛卡尔积，因为subquery还是一张表

需要用as_scalar()
session.query(UserType,session.query(Users).as_scalar())


## relationship
非常重要，谁有foreign key 就把relationship写在哪里

- 1.正向操作
- 2.反向操作

问题1.获取用户信息以及与其关联的用户类型名称
user_list = session.query(Users).all()
for row in user_list:
    print(row.id,row.name,row.email,row.uuser_type_id)


user_list = session.query(Users.name,UserType.title).join(UserType,isouter=True).all()
for row in user_list:
    print(row)

不加all，就是一个迭代器
加all，就是全部在内存中了，相当于fetchall ,fetchone

user_type = relationship("UserType",backref='xxoo')
result = session.query(Users)
for row in result:
    print(row.user_type.title)

问题2:获取用户类型

type_list = session.query(UserType)
for row in type_list:
    print(row.id,row.title,row.xxoo)
