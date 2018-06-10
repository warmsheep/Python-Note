## 基本数据类型
* 数字类型

  * int
create table t1(
    id unsigned int,
    name char(10),
) engine=innodb default charset=utf8;

create table t1(
    id signed int,
    name char(10),
) engine=innodb default charset=utf8;
 有符号
  
  *
  无符号
  *
  * tinyint
    有符号
    * -128~127
    无符号
    * 0~255
    特别的:mysql中的无布尔值，使用tinyint(1)构造。
bigint
smallint
float(不太精准的)
double(不太精准的)
decimal

字符类型
创建数据表时，定长的列往前放

* char(10) 速度快
不够会补空格
* varchar(10) 节省空间
* text
上传文件:
  文件存硬盘
  db存路径

图片存储一般用路径来存

* enum枚举类型
create table shirts(
    name varchar(10),
    size enum('xs','s','m','l','xl')
  )
insert into shirts(name,size) values('alex','l')
* set集合类型

create table myset(
  name varchar(40),
  col set('a','b','c','d')
)

insert into myset(name,col) values('ake','a,c')

时间类型
* date
* time
* datetime

二进制类型
