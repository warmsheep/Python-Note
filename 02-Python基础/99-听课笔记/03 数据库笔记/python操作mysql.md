# python操作MySQL方法
Python操作MySQL主要使用两种方式：
* 原生模块 pymsql
* ORM框架 SQLAchemy

## pymysql(稍后补充)



## sqlalchemy 和 ORM
### Part I: 基础知识
#### 简介：
SQLAlchemy是Python编程语言下的一款ORM框架，该框架建立在数据库API之上，使用关系对象映射进行数据库操作，简言之便是：将对象转换成SQL，然后使用数据API执行SQL并获取执行结果。

ORM：Object Relationl Mapping，对象关系映射。
* ORM 将 数据库中的表 与 面向对象语言中的类 建立了一种对应关系。
* 为了保证一致的使用习惯，通过orm将编程语言的对象模型和数据库的关系模型建立映射关系
* 这样我们在使用编程语言对数据库进行操作的时候可以直接使用编程语言的对象模型进行操作就可以了， 而不用直接使用sql语言。

#### ORM作用：
* 隐藏了数据访问细节，“封闭”的通用数据库交互，ORM的核心。使得通用数据库交互变得简单，并且不会考虑SQL语句。快速开发
* ORM使我们构造固化数据库结构变得简单。

#### ORM缺点：
* 自动化意味着映射和关联管理，代价是牺牲性能
* 现在的各种ORM框架都在尝试使用各种方法来减轻这块(LazyLoad, Cache)，效果还是很显著的。

![sqpalchem原理](image/sqlalchemy原理.png)

#### sqlalchemy流程如下：
1. 
2.




### Part II: 
#### 安装：
```shell
pip3 install sqlalchemy
```

#### sqlalchemy说明：
* sqlalchemy底层还是对mysqldb，pymysql的封装
* 不用写原生SQL，但是sqlalchemy执行的时候还是要用原生sql
* sqlalchemy就是通过使用mysqldb，pymysql等来执行原生sql


#### 创建表
1. 使用原生sql语句

```sql
CREATE TABLE user (
　　　　　　　　　　id INTEGER NOT NULL AUTO_INCREMENT,
　　　　　　　　　　name VARCHAR(32),
　　　　　　　　　　password VARCHAR(64),
　　　　　　　　　　PRIMARY KEY (id)
　　　　　　　　)
```

2. 使用sqlalchemy创建表的两种方法
