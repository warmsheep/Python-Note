## http协议

CS模式 client--server

基于TCP协议(三次握手) UDP协议

socket与TCP协议的关系--(socket是对TCP UDP协议的封装(传输层))

web服务
标准的cs模式--bs模式

HTTP协议基于tcp协议
tcp完成底层硬件上的连接
http基于tcp协议进行交流，发数据的时候按照这个协议进行交流。

### HTTP协议:
超文本传输协议。这个协议详细规定了浏览器和万维网服务器之间互相通信的规则。
HTTP协议就是一个通信规则，通信规则规定了客户端发送给服务器的内容格式，也规定了服务器发送给客户端的内容格式，其实我们要学习的就是这两个格式！客户端发送给服务器的格式叫"请求协议"；服务器发送给客户端的格式叫"响应协议"。

特点
* HTTP叫超文本传输协议，基于请求/响应模式的
* HTTP是无状态协议(比如打开京东网页刷新了三次，这三次是没有区别的，都是相互独立并且相同的)

URL：统一资源定位符，就是一个网址:  协议名://域名:端口/路径，例如:http://www.oldboy.cn:80/index.html

DNS域名解析，url会把域名解析成一个IP地址

### 一、请求协议(浏览器--->server)
请求协议的格式如下:

(1)请求首行
 请求方式 请求内容 协议版本
```
GET /favicon.ico HTTP/1.1
```

(2)请求头信息  
打开京东，京东打开后，浏览器和京东服务器就断了
connection:keep-alive 长链接，3000ms内还可以等链接，3s之后就会断开
请求头:键值对的形式
User-Agent:标识当前环境的
Accept:能处理什么样的文件，如果是text/html说明浏览器只能渲染html的格式
Accept-Encoding:能接受什么编码，gzip(压缩的格式)
Accept-Language:支持什么语言zh-CN(简体中文)，

最重要的俩
Referer:这次访问的来源处，如果是直接输入网址，没有referer,
盗链:盗链是指服务提供商自己不提供服务的内容，通过技术手段绕过其它有利益的最终用户界面（如广告），直接在自己的网站上向最终用户提供其它服务提供商的服务内容，骗取最终用户的浏览和点击率。受益者不提供资源或提供很少的资源，而真正的服务提供商却得不到任何的收益。
反盗链:用referer来取

Cookie:浏览器带的缓存，再次访问会传输给服务器，http协议是无状态协议的，利用cookie把一些状态或者信息保存起来，cookie想成一个字典，可以存放多组键值对，后面会将这个到底有什么用

```
Host: 127.0.0.1:8080
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36
Accept: */*
Referer: http://127.0.0.1:8080/
Accept-Encoding: gzip, deflate, sdch, br
Accept-Language: zh-CN,zh;q=0.8
Cookie:sessionid=e0ci3j4mwkg8itrtr5so824raj8wilfk;csrftoken=0nNXMorXRmbll9pDD1mEWAlUmqPLPDOMvY5zQy



```

(3)空行

(4)请求体(请求数据)
信息放在封皮就相当于在url地址栏
get请求体不存在，会放在url上面 url:www.baidu.com?a=1(问号隔开地址和参数，参数之间的隔开用&)
post请求才会放在请求体发送过去

#### GET请求
HTTP默认的请求方法就是GET
* 没有请求体
* 数据必须在1k之内
* GET请求会暴露在浏览器的地址栏中

GET请求常用操作
* 在浏览器的地址栏中直接给出URL，那么就一定是GET请求
* 点击页面上的超链接也一定是GET请求
* 提交表单时，表单默认使用GET请求，但可以设置为POST

### POST请求
* 数据不会出现在地址栏中
* 数据的大小没有上限
* 有请求体
* 请求体重如果存在中文，会使用URL编码
```
username=%E5%BC%A0%E%89&password=123
```

### 问题:为什么要进行URL编码？


### 二、响应协议(server--->浏览器)
(1)响应首行 HTTP/1.1，不能默认，发送信息一定要带着相应首行

(2)响应头信息 可以不写，很多都是默认格式

Request Method:访问的请求，get请求
Status Code:200代表请求是成功的，还有404
Remote Address:远程连接IP和端口
Content-Type:数据类型和编码，返回的数据类型
Server:具体的服务器软件的名字，WSGIServer/0.2

```
Request URL:http://127.0.0.1:8090/login/
Request Method:GET
Status Code:200 OK
Remote Address:127.0.0.1:8090
Response Headers
view source
Content-Type:text/html; charset=utf-8
Date:Wed, 26 Oct 2016 06:48:50 GMT
Server:WSGIServer/0.2 CPython/3.5.2
X-Frame-Options:SAMEORIGIN

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form action="/login/" method="post">
  用户名：<input type="text" name="username"/>
  <input type="submit" value="提交"/>
</form>    
</body>
</html>
```

Set-Cookie:SESSIONID=...
(3)空行

(4)响应体

状态码
200:
404:
500:请求资源找到了，但服务器内部出现了错误;(以5开头都是服务器出了问题)
302:重定向，当响应吗为302时，表示服务器要求浏览器重新再发一个请求，服务器会发送一个响应头Location，他指定了心情求的URL地址
304:Last-Modified需要补充一下

### 其他响应头
告诉浏览器不要缓存的响应头：

Expires: -1；
Cache-Control: no-cache；
Pragma: no-cache；
自动刷新响应头，浏览器会在3秒之后请求http://www.baidu.com：

Refresh: 3;url=http://www.baidu.com 
