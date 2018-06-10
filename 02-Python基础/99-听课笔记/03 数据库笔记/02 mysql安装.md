## mysql安装
### windows
* 可执行文件
  * 点点点
* 压缩包
  * 放置任意目录
  * 初始化
    * 服务端:mysqld

    ```
    mysqld地址（本篇所有的地址均不需要.exe） --initialise-insecure
    #会创建一个用户名:root 密码:无密码
    ```
  * 启动服务端(启动等待客户端连接)
    ```
    mysqld
    ```
  * 客户端
    ```
    mysql -u root -p
    ```

  * 发送指令
  show database;
  create database db1;
  * 配置环境变量


  * windows服务(两步需要一起)
    找到路径 --install
      找到路径 --remove
    net start mysql


    net stop mysql
* mysqld.exe:服务端
* mysql.exe:客户端
