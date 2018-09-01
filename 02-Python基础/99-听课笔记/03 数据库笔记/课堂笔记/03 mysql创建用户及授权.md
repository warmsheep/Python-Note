## mysql创建用户及授权
2.关于连接
  * 文件夹(数据库)
    * 文件(表)
      * 数据行(行)
连接:
  show databases;
  use 数据库名称;
  show tables;
  select * from 表名;
  select name,age,id from 表名;


默认: 用户root
创建:
  create user 'peqi'@'102.168.1.1' identified by '123123'
  create user 'peqi'@'102.168.1.%' identified by '123123'
  create user 'peqi'@'%' identified by '123123'
授权:
  权限   人
  grant 权限
  grant select,insert,update on db1.* to 'alex'@'%';
  grant all privileges on db1.t1 to 'alex'@'%';(除去grant权限的所有权限)
取消授权
  revoke 权限 on 数据库 from 用户
创建的用户都放在了mysql的文件夹里面
use mysql;
show tables;

www.cnblogs.com/wupeqi/articles/5713315.html
