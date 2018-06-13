## 一、HTTP协议
```
CS模式 client--server

基于TCP协议(三次握手) UDP协议

socket与TCP协议的关系--(socket是对TCP UDP协议的封装(传输层))

web服务
标准的cs模式--bs模式

HTTP协议基于tcp协议
tcp完成底层硬件上的连接
http基于tcp协议进行交流，发数据的时候按照这个协议进行交流。
```

超文本传输协议。这个协议详细规定了浏览器和万维网服务器之间互相通信的规则。
HTTP协议就是一个通信规则，通信规则规定了客户端发送给服务器的内容格式，也规定了服务器发送给客户端的内容格式，其实我们要学习的就是这两个格式！客户端发送给服务器的格式叫"请求协议"；服务器发送给客户端的格式叫"响应协议"。

**特点**
* HTTP叫超文本传输协议，基于请求/响应模式的
* HTTP是无状态协议(比如打开京东网页刷新了三次，这三次是没有区别的，都是相互独立并且相同的)

URL：统一资源定位符，就是一个网址:  协议名://域名:端口/路径，例如:http://www.oldboy.cn:80/index.html

DNS域名解析，会把域名解析成一个IP地址

## 二、请求协议(浏览器--->server)
请求协议的格式如下:

(1)请求首行:请求方式 请求内容 协议版本
```
GET /favicon.ico HTTP/1.1
```

(2)请求头信息:请求头名称:请求头内容，即为key:value格式
打开京东，京东打开后，浏览器和京东服务器就断了
connection:keep-alive 长链接，3000ms内还可以等链接，3s之后就会断开
请求头:键值对的形式
User-Agent:标识当前环境
Accept:能处理什么样的文件，如果是text/html说明浏览器只能渲染html的格式
Accept-Encoding:能接受什么编码，gzip(压缩的格式)
Accept-Language:支持什么语言zh-CN(简体中文)，

最重要的俩
Referer:这次访问的来源处，如果是直接输入网址，则没有referer,
盗链:盗链是指服务提供商自己不提供服务的内容，通过技术手段绕过其它有利益的最终用户界面（如广告），直接在自己的网站上向最终用户提供其它服务提供商的服务内容，骗取最终用户的浏览和点击率。受益者不提供资源或提供很少的资源，而真正的服务提供商却得不到任何的收益。
反盗链:用referer来取访问的来源处，再进行限制

Cookie:浏览器带的缓存，再次访问会传输给服务器，然后服务器再传送给浏览器，http协议是无状态协议的，利用cookie把一些状态或者信息保存起来，cookie想成一个字典，可以存放多组键值对，后面会讲这个到底有什么用，JSESSIONID=369766FDF6220F7803433C0B2DE36D98：因为不是第一次访问这个地址，所以会在请求中把上一次服务器响应中发送过来的Cookie在请求中一并发送去过；这个Cookie的名字为JSESSIONID。

```
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding:gzip, deflate, sdch
Accept-Language:zh-CN,zh;q=0.8
Cache-Control:no-cache
Connection:keep-alive
Cookie:csrftoken=z5H43ZwARx7AIJ82OEizBOWbsAQA2LPk
Host:127.0.0.1:8090
Pragma:no-cache
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36
Name
login/
requests ❘ 737 B transferred ❘ Finish: 5 ms ❘ DOMContentLoaded: 14 ms ❘ Load: 14 ms



```

(3)空行

(4)请求体(请求数据)
信息放在封皮就相当于在url地址栏
get没有请求体，会放在url上面 url:www.baidu.com?a=1(问号隔开地址和参数，参数之间的隔开用&)
post请求才会放在请求体发送过去

浏览器发送给服务器的内容就这个格式的，如果不是这个格式服务器将无法解读！在HTTP协议中，请求有很多请求方法，其中最为常用的就是GET和POST。不同的请求方法之间的区别，后面会一点一点的介绍。

### 2.1 GET请求
HTTP默认的请求方法就是GET
* 没有请求体
* 数据必须在1k之内
* GET请求会暴露在浏览器的地址栏中

GET请求常用操作
* 在浏览器的地址栏中直接给出URL，那么就一定是GET请求
* 点击页面上的超链接也一定是GET请求
* 提交表单时，表单默认使用GET请求，但可以设置为POST

```
HTTP无状态：无状态是指协议对于事务处理没有记忆能力，服务器不知道客户端是什么状态。从另一方面讲，打开一个服务器上的网页
和你之前打开这个服务器上的网页之间没有任何联系
如果你要实现一个购物车，需要借助于Cookie或Session或服务器端API（如NSAPI and ISAPI）记录这些信息，请求服务器结算页面时同时将这些信息提交到服务器
当你登录到一个网站时，你的登录状态也是由Cookie或Session来“记忆”的，因为服务器并不知道你是否登录
优点：服务器不用为每个客户端连接分配内存来记忆大量状态，也不用在客户端失去连接时去清理内存，以更高效地去处理WEB业务
缺点：客户端的每次请求都需要携带相应参数，服务器需要处理这些参数

容易犯的误区：
1、HTTP是一个无状态的面向连接的协议，无状态不代表HTTP不能保持TCP连接，更不能代表HTTP使用的是UDP协议（无连接）
2、从HTTP/1.1起，默认都开启了Keep-Alive，保持连接特性，简单地说，当一个网页打开完成后，客户端和服务器之间用于传输
HTTP数据的TCP连接不会关闭，如果客户端再次访问这个服务器上的网页，会继续使用这一条已经建立的连接
3、Keep-Alive不会永久保持连接，它有一个保持时间，可以在不同的服务器软件（如Apache）中设定这个时间
```


### 2.2 POST请求
* 数据不会出现在地址栏中
* 数据的大小没有上限
* 有请求体
* 请求体中如果存在中文，会使用URL编码

```
username=%E5%BC%A0%E%89&password=123
```

#### 为什么要进行URL编码？
```
我们都知道Http协议中参数的传输是"key=value"这种简直对形式的，如果要传多个参数就需要用“&”符号对键值对进行分割。如"?name1=value1&name2=value2"，这样在服务端在收到这种字符串的时候，会用“&”分割出每一个参数，然后再用“=”来分割出参数值。


针对“name1=value1&name2=value2”我们来说一下客户端到服务端的概念上解析过程:
  上述字符串在计算机中用ASCII吗表示为：
  6E616D6531 3D 76616C756531 26 6E616D6532 3D 76616C756532。
   6E616D6531：name1
   3D：=
   76616C756531：value1
   26：&
   6E616D6532：name2
   3D：=
   76616C756532：value2
   服务端在接收到该数据后就可以遍历该字节流，首先一个字节一个字节的吃，当吃到3D这字节后，服务端就知道前面吃得字节表示一个key，再想后吃，如果遇到26，说明从刚才吃的3D到26子节之间的是上一个key的value，以此类推就可以解析出客户端传过来的参数。

   现在有这样一个问题，如果我的参数值中就包含=或&这种特殊字符的时候该怎么办。
比如说“name1=value1”,其中value1的值是“va&lu=e1”字符串，那么实际在传输过程中就会变成这样“name1=va&lu=e1”。我们的本意是就只有一个键值对，但是服务端会解析成两个键值对，这样就产生了奇异。

如何解决上述问题带来的歧义呢？解决的办法就是对参数进行URL编码
   URL编码只是简单的在特殊字符的各个字节前加上%，例如，我们对上述会产生奇异的字符进行URL编码后结果：“name1=va%26lu%3D”，这样服务端会把紧跟在“%”后的字节当成普通的字节，就是不会把它当成各个参数或键值对的分隔符。
```

使用表单可以发POST请求，但表单默认是GET
```html
<form action="" method="post">
  关键字：<input type="text" name="keyword"/>
  <input type="submit" value="提交"/>
</form>
```

```http
Request Headers
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding:gzip, deflate
Accept-Language:zh-CN,zh;q=0.8
Cache-Control:no-cache
Connection:keep-alive
Content-Length:13
Content-Type:application/x-www-form-urlencoded
Cookie:csrftoken=z5H43ZwARx7AIJ82OEizBOWbsAQA2LPk
Host:127.0.0.1:8090
Origin:http://127.0.0.1:8090
Pragma:no-cache
Referer:http://127.0.0.1:8090/login/
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1)
           AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36

Form Data
username:yuan
```

POST请求是可以有体的，而GET请求不能有请求体。
* Referer: http://localhost:8080/hello/index.jsp：请求来自哪个页面，例如你在百度上点击链接到了这里，那么Referer:http://www.baidu.com；如果你是在浏览器的地址栏中直接输入的地址，那么就没有Referer这个请求头了；

* Content-Type: application/x-www-form-urlencoded：表单的数据类型，说明会使用url格式编码数据；url编码的数据都是以“%”为前缀，后面跟随两位的16进制。

* Content-Length:13：请求体的长度，这里表示13个字节。

* keyword=hello：请求体内容！hello是在表单中输入的数据，keyword是表单字段的名字。

```
Referer请求头是比较有用的一个请求头，它可以用来做统计工作，也可以用来做防盗链。
统计工作：我公司网站在百度上做了广告，但不知道在百度上做广告对我们网站的访问量是否有影响，那么可以对每个请求中的Referer进行分析，如果Referer为百度的很多，那么说明用户都是通过百度找到我们公司网站的。
防盗链：我公司网站上有一个下载链接，而其他网站盗链了这个地址，例如在我网站上的index.html页面中有一个链接，点击即可下载JDK7.0，但有某个人的微博中盗链了这个资源，它也有一个链接指向我们网站的JDK7.0，也就是说登录它的微博，点击链接就可以从我网站上下载JDK7.0，这导致我们网站的广告没有看，但下载的却是我网站的资源。这时可以使用Referer进行防盗链，在资源被下载之前，我们对Referer进行判断，如果请求来自本网站，那么允许下载，如果非本网站，先跳转到本网站看广告，然后再允许下载。
```


## 三、响应协议(server--->浏览器)
### 3.1 响应内容
(1)响应首行 HTTP/1.1，不能默认，发送信息一定要带着相应首行

(2)响应头信息 可以不写，很多都是默认格式


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
* HTTP/1.1 200 OK：响应协议为HTTP1.1，状态码为200，表示请求成功，OK是对状态码的解释；

* Server:WSGIServer/0.2 CPython/3.5.2：服务器的版本信息；

* Content-Type: text/html;charset=UTF-8：响应体使用的编码为UTF-8；

* Content-Length: 724：响应体为724字节；

* Set-Cookie: JSESSIONID=C97E2B4C55553EAB46079A4F263435A4; Path=/hello：响应给客户端的Cookie；
Date: Wed, 25 Sep 2012 04:15:03 GMT：响应的时间，这可能会有8小时的时区差；


(3)空行

(4)响应体

状态码
200:
404:
500:请求资源找到了，但服务器内部出现了错误;(以5开头都是服务器出了问题)
302:重定向，当响应吗为302时，表示服务器要求浏览器重新再发一个请求，服务器会发送一个响应头Location，他指定了心情求的URL地址
304:Last-Modified需要补充一下


响应内容是由服务器发送给浏览器的内容，浏览器会根据响应内容来显示。遇到<img src=''>会开一个新的线程加载，所以有时图片多的话，内容会先显示出来，然后图片才一张张加载出来。

### 3.2 状态码
响应头对浏览器来说很重要，它说明了响应的真正含义。例如200表示响应成功了，302表示重定向，这说明浏览器需要再发一个新的请求。

* 200：请求成功，浏览器会把响应体内容（通常是html）显示在浏览器中；

* 404：请求的资源没有找到，说明客户端错误的请求了不存在的资源；

* 500：请求资源找到了，但服务器内部出现了错误；

* 302：重定向，当响应码为302时，表示服务器要求浏览器重新再发一个请求，服务器会发送一个响应头Location，它指定了新请求的URL地址；

* 304：
```
当用户第一次请求index.html时，服务器会添加一个名为Last-Modified响应头，这个头说明了
  index.html的最后修改时间，浏览器会把index.html内容，以及最后响应时间缓存下来。当用户第
  二次请求index.html时，在请求中包含一个名为If-Modified-Since请求头，它的值就是第一次请
  求时服务器通过Last-Modified响应头发送给浏览器的值，即index.html最后的修改时间，
  If-Modified-Since请求头就是在告诉服务器，我这里浏览器缓存的index.html最后修改时间是这个,
  您看看现在的index.html最后修改时间是不是这个，如果还是，那么您就不用再响应这个index.html
  内容了，我会把缓存的内容直接显示出来。而服务器端会获取If-Modified-Since值，与index.html
  的当前最后修改时间比对，如果相同，服务器会发响应码304，表示index.html与浏览器上次缓存的相
  同，无需再次发送，浏览器可以显示自己的缓存页面，如果比对不同，那么说明index.html已经做了修
  改，服务器会响应200。
```

![浏览器请求](https://images2015.cnblogs.com/blog/877318/201610/877318-20161026162455218-1166783413.png)

### 3.3 其他响应头
告诉浏览器不要缓存的响应头：

* Expires: -1；
* Cache-Control: no-cache；
* Pragma: no-cache；

自动刷新响应头，浏览器会在3秒之后请求http://www.baidu.com：

* Refresh: 3;url=http://www.baidu.com


### 3.4 HTML中指定响应头

在HTMl页面中可以使用<meta http-equiv="" content="">来指定响应头，例如在index.html页面中给出<meta http-equiv="Refresh" content="3;url=http://www.baidu.com">，表示浏览器只会显示index.html页面3秒，然后自动跳转到http://www.baidu.com.
