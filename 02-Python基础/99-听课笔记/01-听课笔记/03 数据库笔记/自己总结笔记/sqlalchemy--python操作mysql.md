# python操作MySQL方法
Python操作MySQL主要使用两种方式：
* 原生模块 pymsql
* ORM框架 SQLAchemy

## sqlalchemy
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

![sqpalchem原理](../image/sqlalchemy原理.png)

### PartII: 架构与流程
#### sqlalchemy流程
1. 使用者通过ORM对象提交命令
2. 将命令交给sqlalchemy core转换为SQL
3. 使用 Engine/ConnectionPooling/Dialect 进行数据库操作
  3.1. 匹配使用者事先配置好的egine
  3.2. egine从连接池中取出一个链接
  3.3. 基于该链接通过Dialect调用DB API，将SQL转交给它去执行

总结：流程大致可以分为两个阶段：
第一阶段(流程1-2)：将sqlalchemy的对象转换为SQL语句
第二阶段(流程3)：将sql语句交给数据库去执行


#### DB API
sqlAche本身不能操作数据库，其必须以pymysql等第三方插件，Dialect用于和数据API进行交流，根据配置文件的不同调用不同的数据库API，从而实现对数据库的操作，如：

```Python
#1、MySQL-Python
    mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>

#2、pymysql
    mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]

#3、MySQL-Connector
    mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>

#4、cx_Oracle
    oracle+cx_oracle://user:pass@host:port/dbname[?key=value&key=value...]
```


### Part II: 
#### 安装：
```shell
pip3 install sqlalchemy
```


#### sqlalchemy说明：
* sqlalchemy底层还是对mysqldb，pymysql的封装
* 不用写原生SQL，但是sqlalchemy执行的时候还是要用原生sql
* sqlalchemy就是通过使用mysqldb，pymysql等来执行原生sql


#### 创建表
1.使用原生sql语句

```sql
CREATE TABLE user (
　　　　　　　　　　id INTEGER NOT NULL AUTO_INCREMENT,
　　　　　　　　　　name VARCHAR(32),
　　　　　　　　　　password VARCHAR(64),
　　　　　　　　　　PRIMARY KEY (id)
　　　　　　　　)
```

2.使用sqlalchemy创建表的两种方法
ORM中
* 类 ===> 表
* 对象 ==> 表中的一行记录
##### 第一种：在自定义继承declarative_base这个基类来映射数据表
```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

# 1. create_engine是连接数据库的引擎
# 2.mysql+pymsql指定使用pymysql来执行原生sql
# 3.//root:1@10.1.0.51/tomdb   <<==>> //用户名：密码@ip:端口/数据库名
# 4.encoding='utf-8' 指定创建的表用‘utf-8'编码（可以存中文）
# 5.echo=True 将执行SQL原生语句的执行细节打印出来

engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/t1", max_overflow=5, echo=True)

# 生成orm基类，执行SQL语句的类就继承Base
Base = declarative_base()

# 创建单表
# 这里仅仅是声明如何定义，到这一步并未执行
class Users(Base):
    __tablename__ = 'users' #表名
    id = Column(Integer, primary_key=True) #Column是导入的模块
    name = Column(String(32)) #String也是导入的模块
    extra = Column(String(16))

    __table_args__ = (
    UniqueConstraint('id', 'name', name='uix_id_name'),
        Index('ix_id_name', 'name', 'extra'),
    )

    def __repr__(self):
      #如果想让它变的可读，只需在定义表的类下面加上这样的代码
        return "<id:%s name:%s>\n"%(self.id, self.name)

# 一对多
class Favor(Base):
    __tablename__ = 'favor'
    nid = Column(Integer, primary_key=True)
    caption = Column(String(50), default='red', unique=True)


class Person(Base):
    __tablename__ = 'person'
    nid = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=True)
    favor_id = Column(Integer, ForeignKey("favor.nid"))

# 多对多
class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    port = Column(Integer, default=22)

class Server(Base):
    __tablename__ = 'server'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)


class ServerToGroup(Base):
    __tablename__ = 'servertogroup'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    server_id = Column(Integer, ForeignKey('server.id'))
    group_id = Column(Integer, ForeignKey('group.id'))

def init_db():
    Base.metadata.create_all(engine) #创建表结构,执行create_all(engine)将会执行所有继承Base的语句

def drop_db():
    Base.metadata.drop_all(engine)
```

#### 操作表

```Python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

'''第一步：连接数据库'''
engine = create_engine("mysql+pymysql://root:@127.0.0.1/tb1?charset=utf8")

'''附加: 无论是增删改查都要先创建与数据库的会话session class'''
# 创建与数据库的会话session class ,注意,这里返回给session的是个class类,不是实例
Session_class = sessionmaker(bind=engine)       #创建用于数据库session的类
session = Session_class()                       #这里才是生成session实例可以理解为cursor


'''第二步：操作数据库'''
# 1、查看mysql中有哪些数据库
dbs=session.execute('show databases;').fetchall()

# 2、切换当前数据库
session.execute('use tb1;')

# 3、查询时过滤出第一条
row1=session.execute('select * from classes where id=1;').first()
print(row1.title)
#Java开发33
```

```Python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 表结构
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/t1", max_overflow=5)

Base = declarative_base()

# 创建单表
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    extra = Column(String(16))

    __table_args__ = (
    UniqueConstraint('id', 'name', name='uix_id_name'),
        Index('ix_id_name', 'name', 'extra'),
    )

    def __repr__(self):
        return "%s-%s" %(self.id, self.name)

# 一对多
class Favor(Base):
    __tablename__ = 'favor'
    nid = Column(Integer, primary_key=True)
    caption = Column(String(50), default='red', unique=True)

    def __repr__(self):
        return "%s-%s" %(self.nid, self.caption)

class Person(Base):
    __tablename__ = 'person'
    nid = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=True)
    favor_id = Column(Integer, ForeignKey("favor.nid"))
    # 与生成表结构无关，仅用于查询方便
    favor = relationship("Favor", backref='pers')

# 多对多
class ServerToGroup(Base):
    __tablename__ = 'servertogroup'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    server_id = Column(Integer, ForeignKey('server.id'))
    group_id = Column(Integer, ForeignKey('group.id'))
    group = relationship("Group", backref='s2g')
    server = relationship("Server", backref='s2g')

class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    port = Column(Integer, default=22)
    # group = relationship('Group',secondary=ServerToGroup,backref='host_list')


class Server(Base):
    __tablename__ = 'server'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)

def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)

#数据库连接
Session = sessionmaker(bind=engine)
session = Session()
```




##### 第二种：通过模式声明，通过__table__可以查看定义表元数据
* 基本不用这种方式

```Python
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapper

metadata = MetaData()

user = Table('user', metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String(50)),
            Column('fullname', String(50)),
            Column('password', String(12))
        )

class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

mapper(User, user)
```

### Part III: 操作
#### 增

```python
obj = Users(name='alex0', extra='sb')
# 增加单行记录，用add方法
session.add(obj)
# 增加多行记录，用send_all，但是必须用列表来存放数据
session.add_all([
 Users(name='alex1', extra='sb1'),
 Users(name='alex2', extra='sb2')
 ])
 # 增加完记录，一定要commit，才能提交到数据库
session.commit()   
```

#### 删

```python
# session.query(表类名).filter(查询条件).delete()
# 删除单条数据
session.query(Users).filter(Users.id > 2).delete()
session.commit()

# 删除多条数据
session.query(Users).filter((Users.id.in_([4,5,6])).delete(synchronize_session=False)
'''synchronize_session=False 删除时不进行session同步，在session commit或者expire_all之前，这些被删除的对象都存在session中。'''
session.commit()
```

#### 改
```python
session.query(Users).filter(Users.id > 2).update({"name" : "099"})
session.query(Users).filter(Users.id > 2).update({Users.name: Users.name + "099"}, synchronize_session=False)
session.query(Users).filter(Users.id > 2).update({"num": Users.num + 1}, synchronize_session="evaluate")
session.commit()
```

#### 简单查找
```Python
#1 打印user表中所有数据
ret = Session.query(User).all()     #user表中所有数据


#2 打印user表中所有name=jack的用户
ret = Session.query(User).filter_by(name='jack').all()

#3 打印user表中第一条name=jack的用户
ret = Session.query(User).filter_by(name='jack').first()     

#4 单条件查询
data4 = Session.query(User).filter(User.id<100).all()
data5 = Session.query(User).filter(User.id==2).all()
data6 = Session.query(User).filter_by(id=2).all()

#5 filter多条件查询
# filter可以链式使用
data7 = Session.query(User).filter(User.id>1).filter(User.id<3).all()
ret = Session.query(User).filter(User.id > 1, User.name == 'jack').all()
ret = Session.query(User).filter(User.id.between(1, 3), User.name == 'jack').all()
"""in_:在...里面（注意in右边有个下划线，而不是直接in，是in_,in_里面是一个列表）"""
ret = Session.query(User).filter(User.id.in_([3,4])).all()

```

#### 高级查找
```python
'''第1步 查： 通配符，like近似查询 '''
ret1 = Session.query(User).filter(User.name.like('j%')).all()

'''第2步 查： 限制（类似于列表切片） '''
ret = Session.query(User)[0:3]        
#这里过滤id但是从0开始计算[0:3]=id从1到4

'''第3步：    排序'''
ret = Session.query(User).order_by(User.id.desc()).all()
ret = Session.query(User).order_by( User.id.asc()).all()
ret = Session.query(User).order_by(User.name.desc(), User.id.asc()).all()
```

#### 分组
```Python
from sqlalchemy import func
ret = Session.query(User).group_by(User.name).all() #有多个同名的只会打印id靠前的yige
ret = Session.query(User.name,func.count(User.name)).group_by(User.name).all()   #[('jack', 2), ('new name', 1), ('tom', 3)]
ret = Session.query(
    func.max(User.id),
    func.sum(User.id),
    func.min(User.id)).group_by(User.name).all()
```

#### 回滚
```python
fake_user = User(name='Rain', password='12345') #创建一个用户
session.add(fake_user)
session.rollback() #此时你rollback一下
session.commit()
```

### Part IV: 一对多外键关联

```python
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATE, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("mysql+pymysql://root:1@127.0.0.1/tomdb?charset=utf8")

'''第一步：   创建表结构'''
Base = declarative_base()      #生成orm基类，执行SQL语句的类就继承Base

class User(Base):
    __tablename__ = 'user'                    #表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32),nullable=False,unique=True)
    register_date = Column(DATE,default='2014-05-21')
    user_type_id = Column(Integer,ForeignKey("user_type.id",ondelete='CASCADE'))    #这里和UserType表的id字段关联
    user_type = relationship("UserType",backref="user", cascade="all, delete-orphan",single_parent=True)          #仅仅是内存中关联关系

    def __repr__(self):
        return "<id:%s name:%s UserType:%s>\n"%(self.id,self.name,self.user_type)

class UserType(Base):
    __tablename__ = "user_type"
    id = Column(Integer, primary_key=True)
    name = Column(String(32),unique=True,nullable=False)
    def __repr__(self):
        return "<用户类型：%s>"%self.name

Base.metadata.create_all(engine) #创建表结构

#注：一对多中，sqlalchemy 联级删除必须要设置下面参数
# ForeignKey中添加：ondelete='CASCADE'
# relationship关联中添加：cascade="all, delete-orphan",single_parent=True

models.py 需要实现一对多联级删除时需要添加参数
```

relationship是为了简化联合查询join等，创建的两个表之间的虚拟关系，这种关系与标的结构时无关的。他与外键十分相似，确实，他必须在外键的基础上才允许使用,不然会报错：

* 前提：存在外键情况下，可以这么操作
  * 只使用外键，需要使用join才可以取出数据:
    ```python
    session.query(表名1).join(表名2).filter(条件).all()
    ```
  * 如果不使用join，也可以连表查询:
    ```python
    session.query(表名1.字段1,表名2.字段2).filter(表名1.字段a==表名2.字段2).filter()
    ```

* 假设：不存在外键情况下，可以这么操作：
```python
query.join(Address, User.id==Address.user_id)    # explicit condition
query.join(User.addresses)                       # specify relationship from left to right
query.join(Address, User.addresses)              # same, with explicit target
query.join('addresses')   
```

ForeignKey表示，Addresses.user_id列的值应该等于users.id列中的值，即，users的主键
relationship(), 它告诉 ORM ,Address类本身应该使用属性Address.user链接到User类

relationship()的参数中有一个称为backref()的relationship()的子函数，反向提供详细的信息, 即在users中添加User对应的Address对象的集合，保存在User.addresses中

两个互补关系, Address.user和User.addresses被称为一个双向关系，并且这是SQLAlchemy ORM的一个关键特性

#### 增
```python
from sqlalchemy.orm import sessionmaker
from orm_test import models

#创建与数据库的会话session class ,注意,这里返回给session的是个class类,不是实例
Session_class = sessionmaker(bind=models.engine)     #创建用于数据库session的类
session = Session_class()                            #这里才是生成session实例可以理解为cursor

#1、创建用户类型
user_type_obj1 = models.UserType(name='内部员工')
user_type_obj2 = models.UserType(name='外部用户')
session.add_all([user_type_obj1,user_type_obj2])
session.commit() #到此才统一提交，创建数据：只有执行这一步增删改才会真正写入硬盘

#2、添加一对多数据的两种方法
user_type_obj = session.query(models.UserType).filter(models.UserType.name=='内部员工').first()
# 法1
user1 = models.User(name="zhangsan",register_date="2014-05-21",user_type=user_type_obj)
user2 = models.User(name="lisi",register_date="2014-03-21",user_type_id=1)  # # # 法2
user3 = models.User(name="wangwu",register_date="2014-02-21",user_type_id=2)
session.add_all([user1,user2,user3])
session.commit()                          
# 到此才统一提交，创建数据：只有执行这一步增删改才会真正写入硬盘
```
#### 查：一对多正向反向查找
```python
from sqlalchemy.orm import sessionmaker
from orm_test import models

Session_class = sessionmaker(bind=models.engine)
session = Session_class()

#先在两表中获取一条数据
user_obj = session.query(models.User).filter(models.User.name=='zhangsan').first()
user_type_obj = session.query(models.UserType).filter(models.UserType.name=='内部员工').first()

#1、正向查找：查找张三用户的用户类型
print('zhangsan用户类型：',user_obj.user_type)

#2、反向查找：查找用户类型为"内部员工",的有哪些
print('内部员工有哪些：',user_type_obj.user)
```

#### 改
```python
from sqlalchemy.orm import sessionmaker
from orm_test import models

Session_class = sessionmaker(bind=models.engine)
session = Session_class()

#先在两表中获取一条数据
user_obj = session.query(models.User).filter(models.User.name=='zhangsan').first()
user_obj2 = session.query(models.User).filter(models.User.name=='lisi').first()
user_type_obj = session.query(models.UserType).filter(models.UserType.name=='外部用户').first()

#1、正向修改的两种方法：将zhangsan的用户类型修改为 "外部用户"
user_obj.user_type = user_type_obj            # 法1: 直接改对象
user_obj.user_type_id = user_type_obj.id      # 法2: 直接改id
session.commit()

#2、反向修改方法：将"外部用户"类型中的用户修改成只有：zhangsan、lisi
user_type_obj.user = [user_obj,user_obj2]
session.commit()
```

#### 删：联级需要在创建表时添加参数
```python
from sqlalchemy.orm import sessionmaker
from orm_test import models

#创建与数据库的会话session class ,注意,这里返回给session的是个class类,不是实例
Session_class = sessionmaker(bind=models.engine)     #创建用于数据库session的类
session = Session_class()                            #这里才是生成session实例可以理解为cursor

#1、删除指定用户
session.query(models.User).filter(models.User.name=='zhangsan').delete()
session.commit()

#2、sqlalchemy 联级删除：删除UserType表中类型"内部员工",在user表中所有类型为"内部员工"的用户全部删除
user_type_obj = session.query(models.UserType).filter(models.UserType.name=='内部员工').delete()
session.commit()
'''
注：一对多中，sqlalchemy 联级删除必须要设置下面参数:
ForeignKey中添加：ondelete='CASCADE'
relationship关联中添加：cascade="all, delete-orphan",single_parent=True
'''
```

### Part V:sqlalchemy多对多关联

```Python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer,String,DATE, ForeignKey

engine = create_engine("mysql+pymysql://root:1@127.0.0.1/tomdb?charset=utf8")
Base = declarative_base()      #生成orm基类，执行SQL语句的类就继承Base

'''1 创建关联表：    第三张表book_m2m_author：用来关联下面的authors和books表'''
# 这张关系表不必使用类创建可以直接使用Table创建，因为这张表创建后不必手动向表中插数据
# 对这张表的维护完全是由ORM自己维护的
# 表中仅有两个字段：book_id关联books表的id，author_id关联authors表的id
# 这张表创建完成后必须要在books表和authors表中指定要到book_m2m_author表查询

book_m2m_author = Table('book_m2m_author', Base.metadata,
                        Column('book_id',Integer,ForeignKey('books.id')),
                        Column('author_id',Integer,ForeignKey('authors.id')),
                        )

'''2 创建books表：    用来存储所有作者的名字 '''
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    pub_date = Column(DATE)
    authors = relationship('Author',secondary=book_m2m_author,backref='books')
'''
    books通过authors关联Author表，Book通过字段secondary去查第三张表：book_m2m_author,用secondary参数来表示关联的表
    backref='books'用来反向查一个作者有多少本书
'''
    def __repr__(self):
        return self.name

'''3 创建authors表    用来存储所有的书 '''
class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return self.name

Base.metadata.create_all(engine)

法1：models.py 自己定义第三张表
```

#### 增
```python
from orm_test import models
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=models.engine)
session = Session_class()

'''第一步：向books表和authors表中分别插入三条数据'''
#1、向books表插入三条书名记录
b1 = models.Book(name="python基础教程",pub_date="2014-05-02")
b2 = models.Book(name="从删库到跑路",pub_date="2014-05-02")
b3 = models.Book(name="wireshark网路分析实战",pub_date="2014-05-02")

#2、向authors表插入三条作者记录
a1 = models.Author(name="Tom")
a2 = models.Author(name="Jack")
a3 = models.Author(name="Fly")

#3、这里指定执行上面的创建表命令
session.add_all([b1,b2,b3,a1,a2,a3])
session.commit()

'''第二步：第三张表：book_m2m_author 中创建 作者与书籍的对应关系'''
b1 = session.query(models.Book).filter(models.Book.name=='python基础教程').first()
b2 = session.query(models.Book).filter(models.Book.name=='从删库到跑路').first()
b3 = session.query(models.Book).filter(models.Book.name=='wireshark网路分析实战').first()

a1 = session.query(models.Author).filter(models.Author.name=='Tom').first()
a2 = session.query(models.Author).filter(models.Author.name=='Jack').first()
a3 = session.query(models.Author).filter(models.Author.name=='Fly').first()

b1.authors = [a1,a2]     # 'python基础教程'这本书的作者有："Tom", "Jack"
a1.books = [b1,b2,b3]    # 作者 "Tom" 出版的书有：python基础教程、从删库到跑路、wireshark网路分析实战
session.commit()
```

#### 查
```python
rom orm_test import models
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=models.engine)
session = Session_class()

b1 = session.query(models.Book).filter(models.Book.name=='python基础教程').first()
a1 = session.query(models.Author).filter(models.Author.name=='Tom').first()

#1、正向查找: "python基础教程"  这本书的所有作者
print( b1.authors )       # [Tom, Jack]

#2、反向查找：作者"Tom" 出版的所有书
print( a1.books )        # [python基础教程, 从删库到跑路, wireshark网路分析实战]
```

#### 改
```python
from orm_test import models
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=models.engine)
session = Session_class()

b1 = session.query(models.Book).filter(models.Book.name=='python基础教程').first()
b2 = session.query(models.Book).filter(models.Book.name=='从删库到跑路').first()
b3 = session.query(models.Book).filter(models.Book.name=='wireshark网路分析实战').first()

a1 = session.query(models.Author).filter(models.Author.name=='Tom').first()
a2 = session.query(models.Author).filter(models.Author.name=='Jack').first()
a3 = session.query(models.Author).filter(models.Author.name=='Fly').first()

'''1、正向修改'''
#1.1 将书籍b1的作者从[Tom, Jack] 修改成只有 [Tom]
print(b1.authors)               # [Tom, Jack]
b1.authors = [a1]
print(b1.authors)               # [Tom]
session.commit()

#1.2 通过books表将authors表中作者 "Tom" 名字改成 "Tom New"
b1.authors[0].name = 'Tom'
session.commit()

'''2、反向修改'''
#2.1 将作者 "Tom" 出版的书籍修改成 [python基础教程, 从删库到跑路]
print(a1.books)                # [python基础教程, 从删库到跑路, wireshark网路分析实战]
a1.books = [b1,b2]
print(a1.books)                # [python基础教程, 从删库到跑路]
session.commit()

#2.2 通过authors表将书籍 "python基础教程"名字修改成 "python基础教程第二版"
a1.books[0].name = "python基础教程第二版"
session.commit()

```

#### 删
```python
from orm_test import models
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=models.engine)
session = Session_class()

b1 = session.query(models.Book).filter(models.Book.name=='python基础教程').first()
a1 = session.query(models.Author).filter(models.Author.name=='Tom').first()

#1、正向删除: 将书籍b1的作者 Tom 删除(只是删除book_m2m_author表中的记录，不会删除authors表中的 'Tom')
print(b1.authors)          # [Tom, Jack]
b1.authors.remove(a1)
print(b1.authors)          # [Jack]
session.commit()

#2、反向删除：
print(a1.books)              # [python基础教程, 从删库到跑路, wireshark网路分析实战]
a1.books.remove(b1)          # [从删库到跑路, wireshark网路分析实战]
print(a1.books)

#3、多对多联级删除: 删除作者时，会把这个作者跟所有书的关联关系数据也自动删除(book_m2m_author中的对应信息)
session.delete(a1)
session.commit()
```

### Part VIL: sqlalchemy执行原生SQL语句
#### 1、执行原生SQL语句
```Python
#! -*- coding:utf8 -*-
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

'''第一步：连接数据库'''
engine = create_engine("mysql+pymysql://root:1@127.0.0.1/bsp?charset=utf8")
# engine = create_engine("mysql+pymysql://root:1@127.0.0.1/tomdb",encoding='utf-8', echo=True)

'''附加: 无论是增删改查都要先创建与数据库的会话session class'''
#创建与数据库的会话session class ,注意,这里返回给session的是个class类,不是实例
Session_class = sessionmaker(bind=engine)       #创建用于数据库session的类
session = Session_class()                       #这里才是生成session实例可以理解为cursor


'''第二步：操作数据库'''
#1、查看mysql中有哪些数据库
dbs=session.execute('show databases;').fetchall()

#2、切换当前数据库
session.execute('use bsp;')

#3、查询时过滤出第一条
row1=session.execute('select * from relations_department where Id>1;').first()
fid_id = row1.fid_id

#4、一对多关联查询: 根据上面查询的父部门id 可以找到父部门信息
row2=session.execute('select * from relations_department where Id=%s;'%fid_id).first()
print row2.name   # 政府事业部

```

#### 2、找到当前数据库中所有非空表

```Python
#! -*- coding:utf8 -*-
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
'''第一步连接数据库'''
engine = create_engine("mysql+pymysql://root:1@127.0.0.1/bsp?charset=utf8")
Session_class = sessionmaker(bind=engine)       #创建用于数据库session的类
session = Session_class()                       #这里才是生成session实例可以理解为cursor


'''第二步：操作数据库'''
#1、查看mysql中有哪些数据库
dbs=session.execute('show databases;').fetchall()

#2、切换当前数据库
session.execute('use bsp;')

#3、查看当前数据库中有哪些表
tables = session.execute('show tables;')

#4、找到当前数据库中所有非空表
tb_list = []
for tb in tables:
    tb_name = tb[0]
    rows = session.execute('select * from %s;'%tb_name)
    row_count = rows.rowcount  # 当前表中数据条数
    if row_count > 1:
        tb_list.append(tb_name)
print(tb_list)
```

ORM
