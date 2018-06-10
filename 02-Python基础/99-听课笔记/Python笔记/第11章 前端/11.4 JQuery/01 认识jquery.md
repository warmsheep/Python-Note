## 认识jquery

### 引入jquery

### JS与jquery区别
1.js是一门编程语言，我们用它来编写客户端浏览器脚本
2.jQuery是js的一个库，包含读个可重用的函数，用来赋值我们简化js开发
3.jQuery能做的js都能做，js能做的，jQuery不一定能做。

注意:一般情况下，是库的文件，该库中都会抛出来构造函数或对象，如果是构造函数，那么使用new关键字创建对象，如果是对象直接调用属性和方法。


### DOM文档的加载顺序
* 1.解析HTML结构
* 2.加载外部样式和样式表文件
* 3.解析并执行脚本代码 （window.onload()外面的代码)
* 4.DOM树构建完成
* 5.加载图片等外部文件
* 6.页面加载完毕

### 执行时间不同
* window.onload必须等到页面 内包括图片的所有元素加载完毕后才执行
* $(document).read()可以同时编写多个，并且都可以得到执行

### 编写个数不同
* window.onload()不能同时编写多个，如果有多个window.onload方法，只会执行一个
* $(document).ready()可以同时编写多个，并且都可以得到执行



### 简化写法不同
* window.onload没有简化写法
* $(document).read(function(){})可以简写成$(function(){})
