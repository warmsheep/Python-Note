## HTML基本结构
浏览器本质上就是一个解释器
## 基础概念知识
### web服务本质
```python
import socket

def main():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost',8081))
    sock.listen(5)

    while True:
        print("server is working.....")
        conn, address = sock.accept()

        request = conn.recv(1024)

        conn.sendall(bytes("HTTP/1.1 201 OK\r\n\r\n<h1>Hello Yuan</h1>","utf8"))
        conn.close()

if __name__ == '__main__':
    main()
```



### html是什么？
* 超文本标记语言(Hypertext Markup language)，通过 **标签语言** 来标记要显示的网页中的各个部分。一套规则，浏览器认识的规则。

* 浏览器按顺序(从上到下，从左到右)渲染网页文件，然后根据标记符解释和显示内容。但需要注意的是，对于不同的浏览器，对同一标签可能会有不完全相同的解释（兼容性）

* 静态网页文件扩展名:.html 或 .htm

### html不是什么？
* HTML不是一种编程语言，而是一种标记语言(makrup language)
* HTML使用标记标签来描述网页

### html结构
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
    </body>
</html>
```
* <!DOCTYPE html>告诉浏览器使用什么样的html或xhtml来解析html文档
* <html></html>是文档的开始标记和结束标记。此元素告诉浏览器自身是一个HTML文档，在它们之间是文档的头部<head>和主体<body>
* <head></head>元素出现在文档的开头部分。<head>与</head>之间的内容不会在浏览器的文档窗口显示，但是其间的元素有特殊重要的意义。<meta charset="utf-8">是指定编码。
* <title></title>定义网页标题，在浏览器标题栏显示
* <body></body>之间的文本是可见的网页主题内容

### html标签格式
* 1 HTML标签是由尖括号包围的关键词，比如<html>
* 2 HTML标签通常是成对出现的(双边标记)，比如<div></div>
* 3 标签不区分大小写。<html>和<HTML>本质是一样的。推荐使用小写。
* 4 标签分为两部分:开始标签<a>和结束标签</a>。两个标签之间的部分，我们叫做标签体。有些标签功能比较简单，使用一个标签即可。这种标签叫做自闭合标签。
* 5 标签可以有若干个属性，也可以不带属性，具体得看标签的，有的可能没有属性，有的有。如<head>元素就不带任何属性
* 6 标签可以嵌套，但是不能交叉嵌套。如错误示例:<a><b></a></b>

标签的语法:
<标签名 属性1="属性值1" 属性2="属性值2"...>内容部分</标签名>
<标签名 属性1="属性值1" 属性2="属性值2".../>

## 基础常用标签
###  <!DOCTYPE>标签
<!DOCTYPE>声明位于文档中的最前面的位置，处于<html>标签之前。此标签可告知浏览器文档使用哪种HTML或XHTML规范。

**作用:** 声明文档的解析类型(document.compatMode)，避免浏览器的怪异模式

**document.compatMode:**
* 1 BackCompat:怪异模式，浏览器使用自己的怪异模式解析渲染页面
* 2 CSS1Compat:标准模式，浏览器使用W3C的标准解析渲染页面。

这个属性会被浏览器识别并使用，但是如果你的页面没有DOCTYP的声明，那么compatMode默认就是BackCompat

### <head>内常用标签
#### <meta>标签
**meta介绍**

* <meta>元素可提供有关页面的元信息(meta-information)，针对搜索引擎和更新频度的描述和关键词。
* <meta>标签位于文档的头部，不包含任何内容
* <meta>提供的信息是用户不可见的

**meta标签的组成:**

meta标签共有两个属性，分别是http-equiv属性和name属性，不同的属性又有不同的参数值，这些不同的参数值就实现了不同的网页功能

* (1)name属性:主要用于描述网页，与之对应的属性值为content,content中的内容主要是便于搜索引擎机器人查找信息和分类信息用的。

name='keywords'--关键词，固定写法，需要和content连用
content='IT培训'

name='description'--描述，固定写法，一般放网站介绍
content='该网站用于解决在线学习

```html
<mate name='keywords' content='meta总结，html meta,meta属性，meta跳转'>
<meta name='description' content='老男孩是一家很厉害的培训机构'>
```

* (2)http-equiv属性:相当于http的文件头作用，它可以向浏览器传回一些有用的信息，以帮助正确地显示网页内容，与之对应的属性为content,content中的内容其实就是各个参数的变量值

```html
<meta http-equiv='refresh' content='https://www.baidu.com'>--如果content没有内容，就是三秒刷新
<meta http-equiv="content-type" charset="UTF-8">--响应头
<meta http-equiv = "X-UA-Compatible" content = "IE=EmulateIE7" /> --兼容性
```

### 非<meta>标签
* tilte标签
```html
<title>oldboy</title>
```
* link标签显示图标
设置打开网页时网址前面的小图标
```html
<link rel="icon" href="http://www.jd.com/favicon.ico">
```
* link引入CSS标签
```html
<link rel="stylesheet" href="css.css">
```
* script引入js标签
```html
<script src="hello.js"></script>　
```

### <body>内常用标签
#### 基本标签
* 1.<hn>: n的取值范围是1~6; 独占一行，从大到小.用来表示标题.
* 2.<p>: 段落标签. 独占一行，包裹的内容被换行.并且也上下内容之间有一行空白.
* 3.<b> <strong>: 加粗标签.
* 4.<strike>: 为文字加上一条中线，删除线.
* 5.<em> <i>: 文字变成斜体.
* 6.<sup>和<sub>: 上角标 和 下角表.
* 7.<br>:换行.
* 8.<hr>:水平线
* 9.特殊字符：&lt; &gt；&quot；&copy;&reg;

### 标签分类
1.块级标签(block):独占一行
  p hn br div
  如何证明，直接给标签加上背景颜色即可
2.内联标签(inline):根据内容而定
  sub sup a br span img
span和div差不多，都没有什么样式，主要用于css布局，不过span是内联的

**块级元素与行内元素的区别**
* 所谓块元素，是以另起一行开始渲染的元素，行内元素则不需另起一行。如果单独在网页中插入这两个元素，不会对页面产生任何的影响。

#### <div>和<span>
这两个元素是专门为定义CSS样式而生的。

* <div></div> ： <div>只是一个块级元素，并无实际的意义。主要通过CSS样式为其赋予不同的表现.
* <span></span>： <span>表示了内联行(行内元素),并无实际的意义,主要通过CSS样式为其赋予不同的表现.


#### 图形标签:<img>
解释器会开一个 **线程**，线程把图片加载出来

* src: 要显示图片的路径.
* alt: 图片没有加载成功时的提示.
* title: 鼠标悬浮时的提示信息.
* width: 图片的宽
* height: 图片的高 (宽高两个属性只用一个会自动等比缩放.)

注意:一般不用img中的height和width，用css来调整


#### 超链接标签(锚标签)<a></a>
**什么是超链接**
所谓的超链接是指从一个网页指向另一个目标的连接关系，这个目标可以是另一个网页，也可以是相同网页上的不同位置，还可以是一个图片，一个电子邮件地址，一个文件，甚至是一个应用程序。

**什么是URL？**
URL是统一资源定位器(Uniform Resource Locator)的缩写，也被称为网页地址，是因特网上标准的资源的地址。

URL举例
http://www.sohu.com/stu/intro.html
http://222.172.123.33/stu/intro.html

**URL地址由4部分组成:**
* 第1部分：为协议：http://、ftp://等
* 第2部分：为站点地址：可以是域名或IP地址
* 第3部分：为页面在站点中的目录：stu
* 第4部分：为页面名称，例如 index.html
各部分之间用“/”符号隔开。

```html
<a href="" target="_blank" >click</a>
```

**href属性指定目标网页地址的类型:**
* 绝对 URL - 指向另一个站点（比如 href="http://www.jd.com）
* 相对 URL - 指当前站点中确切的路径（href="index.htm"）
* 锚 URL - 指向页面中的锚（href="#top"）

**注意:** href=""如果不写任何值，点击a标签相当于刷新


#### 列表标签
**列表标签分类**
* <ul>: 无序列表(unorder list)
```html
<ul>
    <li> 列表项</li>
</ul>
```

* <ol>: 有序列表(order list)
```html
<ol>
    <li> 列表项</li>
</ol>
```

* <dl>: 定义列表
```html
<dl>  定义列表(define list)
    <dt> 列表标题 </dt>(define Title)
    <dd> 列表项 </dd>(define data)
</dl>
```

#### 表格标签: <table>
**表格概念**
表格是一个二维数据空间，一个表格由若干行组成，一个行又有若干单元格组成，单元格里可以包含文字、列表、图案、表单、数字符号、预置文本和其它的表格等内容。

表格最重要的目的是显示表格类数据。表格类数据是指最适合组织为表格格式（即按行和列组织）的数据。

**表格的基本结构:**
* <table>: this is a table
* <th>: table head cell
* <td>: table data cell
* <tr>: table row

```html
<table>
    <tr>
        <th>标题</th>
        <th>标题</th>
    </tr>
    <tr>
        <td>内容</td>
        <td>内容</td>
    </tr>
    <tr>
        <td>内容</td>
        <td>内容</td>
    </tr>
</table>
```


**表格属性:**
* border: 表格边框.
* **cellpadding:** 内边距，调整表格单元格的内容的padding值
* **cellspacing:** 外边距，调整表格单元格之间的间距
* width: 像素 百分比.（最好通过css来设置长宽）
* **rowspan:**  单元格竖跨多少行
* **colspan:**  单元格横跨多少列（即合并单元格）

**注意:** cellspacing和cellpadding都只能在table标签中设置，不能用css设置

* 调整单元格间距
```html
<table border="2px" cellpadding="10px" cellspacing="0px">
    <tr>
        <th>语文</th>
        <th>数学</th>
        <th>英语</th>
        <th>音乐</th>
    </tr>
    <tr>
        <td>80</td>
        <td>90</td>
        <td>100</td>
        <td>95</td>
    </tr>
</table>
```

* 合并表格
```html
<table border="2px" cellpadding="10px" cellspacing="0px">
    <tr>
        <th>语文</th>
        <th>数学</th>
        <th>英语</th>
        <th>音乐</th>
    </tr>
    <tr>
        <td>80</td>
        <td>90</td>
        <td>100</td>
        <td>95</td>
    </tr>
    <tr>
        <td rowspan="2">11</td>
        <td colspan="2">90</td>
        <td>95</td>
    </tr>
    <tr>
        <td>90</td>
        <td>100</td>
        <td>95</td>
    </tr>
</table>
```

#### 表单标签: <form>
form属性:只要form表单的都要有name，不然不能形成键值对

* 功能:表单用于向服务器传输数据，从而实现用户与Web服务器的交互。
* 表单能够包含input系列标签，比如文本字段、复选框、单选框、提交按钮等等。
* 表单还可以包含textarea、select、fieldset和label标签。

**表单属性**
* action: 表单提交到哪.一般指向服务器端一个程序,程序接收到表单提交过来的数据（即表单元素值）作相应处理，比如https://www.sogou.com/web
* method: 表单的提交方式 post/get默认取值就是get。(get和post区别详见HTTP协议笔记)

**表单元素**
**基本概念**
* HTML表单是HTML元素中较为复杂的部分，表单往往和脚本、动态页面、数据处理等功能相结合，因此它是制作动态网站很重要的内容。
* 表单一般用来收集用户的输入信息

**表单工作原理:**
* 访问者在浏览有表单的网页时，可填写必需的信息，然后按某个按钮提交。这些信息通过Internet传送到服务器上。
* 服务器上专门的程序对这些数据进行处理，如果有错误会返回错误信息，并要求纠正错误。当数据完整无误后，服务器反馈一个输入完成的信息

##### <input>系列标签
在form表单之外写input标签没有任何意义

**1 表单类型type**
* text 文本输入框，默认明文，如需要默认值，对value赋值
* password 密码输入框，默认密文
* radio 单选框，一般用来互斥,需要设置name和value属性
* checkbox 多选框,设置默认选项:checked="checked"
* hidden 默认值，不需要用户来选，直接默认
* submit 提交按钮，提交数据，修改submit中提交字样，定义value=""，这个value和提交的value值不一样，并不构成一个键值对
* button 按钮(需要配合js使用.) button和submit的区别？
* file 提交文件：form表单需要加上属性enctype="multipart/form-data"

```
注意:上传文件需要注意两点
 1 请求方式必须是post
 2 enctype="multipart/form-data"
```
**2 表单属性**
* name:表单提交项的键
input类型的表单，都需要加入name属性，没有name属性，则没有意义

```
注意和id属性的区别
  1 name属性是和服务器通信时使用的名称；
  2 而id属性是浏览器端使用的名称，该属性主要是为了方便客户端编程，而在css和javascript中使用的
```
* value:表单提交项的值.
对于不同的输入类型，value 属性的用法也不同：

```
type="button", "reset", "submit" - 定义按钮上的显示的文本
type="text", "password", "hidden" - 定义输入字段的初始值
type="checkbox", "radio", "image" - 定义与输入相关联的值
```

* checked:radio 和 checkbox 默认被选中
* readonly:只读. text 和 password
* disabled: 对所用input都好使.

```html
</p>用户名:<input type="text" name="username"></p> {username:yuan}
</p>密码:<input type="password" name="pwd"></p> {pwd:123}
```

```html
<p>爱好:写作<input type="checkbox" name="habits" value="writing">
        阅读<input type="checkbox" name="habits" value="reading"></p>

{"habits":["writing","reading"]}
```

##### select标签
**select标签结构**
如果属性名和属性值相等，可以直接写属性名即可

```html
<form action="" method="post" name="form1">
    <select name="habbits" multiple size="4">
        <option value="writting" selected>writting</option>
        <option value="walking">walking</option>
        <option value="online">online</option>
        <option value="baseball">baseball</option>
        <option value="haunting">haunting</option>
    </select>
</form>
```

**<select> 下拉选标签属性**
* name:表单提交项的键
* size：选项个数
* multiple：multiple，可以选择多个
* <optgroup>为每一项加上分组，label标签表示分组的名称

**<option>属性：**
* value:表单提交项的值
* selected: selected下拉选默认被选中

##### <textarea> 多行文本框
可以生成一个文本框，并设置文本框的高度和宽度
```html
<form id="form1" name="form1" method="post" action="">
    <textarea cols=“宽度” rows=“高度” name=“名称”>
        默认内容
    </textarea>
</form>
```

##### <label>标签
**定义:**
<label> 标签为 input 元素定义标注（标记）。

**说明:**
* 1 label 元素不会向用户呈现任何特殊效果。
* 2 <label> 标签的 for 属性值应当与相关元素input标签的 id 属性值相同。

```html
<form method="post" action="">
    <label for=“username”>用户名</label>
    <input type=“text” name=“username” id=“username” size=“20” />
</form>
```

##### <fieldset>标签

* fieldset 元素可将表单内的相关元素分组。
* <fieldset> 标签将表单内容的一部分打包，生成一组相关表单的字段。
* 当一组表单元素放到 <fieldset> 标签内时，浏览器会以特殊方式来显示它们，它们可能有特殊的边界、3D 效果，或者甚至可创建一个子表单来处理这些元素。

```html
<fieldset>
    <legend>登录吧</legend>
    <input type="text">
</fieldset>
```

#### form表单与Django交互(暂未更新)
等django学完了再做


### 总结
重点:
* 基础标签
* form表单标签
* table标签
* input标签
