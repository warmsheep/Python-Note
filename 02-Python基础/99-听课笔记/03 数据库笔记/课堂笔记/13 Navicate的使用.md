## navicate

- 使用创建表(外键)
- 新建查询
- 转储sql文件

命令行:
转储sql文件
可以把所有的数据结构和数据导出来

mysqldump也可以转储sql文件
导出:
备份:数据表结构+数据
mysqldump -u root 数据库 > db1.sql -p;
备份:数据表结构
mysqldump -u root -d 数据库 > db1.sql -p;

导入:
mysqldump -u root -p密码 数据库名称<文件名称；
