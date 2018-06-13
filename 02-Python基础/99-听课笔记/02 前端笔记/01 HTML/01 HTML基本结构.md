## HTML基本结构
浏览器本质上就是一个解释器

### html是什么？
html:超文本标记(标签)语言，通过标签语言来标记要显示的网页中的各个部分。一套规则，浏览器认识的规则。

浏览器按顺序(从上到下，从左到右)渲染网页文件，然后根据标记符解释和显示内容。但需要注意的是，对于不同的浏览器，对同一标签可能会有不完全相同的解释（兼容性）

静态网页文件扩展名:.html 或 .htm

### html不是什么？
HTML不是一种编程语言，而是一种标记语言(makrup language)

HTML使用标记标签来描述网页

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
* <head></head>元素出现在文档的开头部分。<head>与</head>之间的内容不会在浏览器的文档窗口显示，但是其间的元素有特殊重要的意义。<meta charset="utf-8">是编码。
* <title></title>定义网页标题，在浏览器标题栏显示
* <body></body>之间的文本是可见的网页主题内容

### html标签格式

1.HTML标签是由尖括号包围的关键词，比如<html>
2.HTML标签通常是成对出现的(双边标记)，比如<div></div>
3.标签不区分大小写。<html>和<HTML>本质是一样的。推荐使用小写。
4.标签分为两部分:开始标签<a>和结束标签</a>。两个标签之间的部分，我们叫做标签体。
  有些标签功能比较简单，使用一个标签即可。这种标签叫做自闭合标签。
5.标签可以有若干个属性，也可以不带属性，具体得看标签的，有的可能没有属性，有的有。如<head>元素就不带任何属性
6.标签可以嵌套，但是不能交叉嵌套。如错误示例:<a><b></a></b>

标签的语法:
<标签名 属性1="属性值1" 属性2="属性值2">

## 常用标签
###  <!DOCTYPE>标签
 <!DOCTYPE>声明位于文档中的最前面的位置，处于<html>标签之前。此标签可告知浏览器文档使用哪种HTML或XHTML规范。

 作用:声明文档的解析类型(document.compatMode)，避免浏览器的怪异模式

 document.compatMode:
 1.BackCompat:怪异模式，浏览器使用自己的怪异模式解析渲染页面
 2.CSS1Compat:标准模式，浏览器使用W3C的标准解析渲染页面。

 这个属性会被浏览器识别并使用，但是如果你的页面没有DOCTYP的声明，那么compatMode默认就是BackCompat

### <head>内常用标签
#### <meta>标签
meta介绍

<meta>元素可提供有关页面的元信息(meta-information)，针对搜索引擎和更新频度的描述和关键词。
<meta>标签位于文档的头部，不包含任何内容
<meta>提供的信息是用户不可见的

meta标签的组成:meta标签共有两个属性，分别是http-equiv属性和name属性，不同的属性又有不同的参数值，这些不同的参数值就实现了不同的网页功能

(1)name属性:主要用于描述网页，与之对应的属性值为content,content中的内容主要是便于搜索引擎机器人查找信息和分类信息用的。

name='keywords'--关键词，固定写法，需要和content连用
content='IT培训'

name='description'--描述，固定写法，一般放网站介绍
content=''
```html
<mate name='keywords' content='meta总结，html meta,meta属性，meta跳转'>
<meta name='description' content='老男孩是一家很厉害的培训机构'>
```

(2)http-equiv属性:相当于http的文件头作用，它可以向浏览器传回一些有用的信息，以帮助正确地显示网页内容，与之对应的属性为content,content中的内容其实就是各个参数的变量值

```html
<meta http-equiv='refresh' content='https://www.baidu.com'>--如果content没有内容，就是三秒刷新
<meta http-equiv="content-type" charset="UTF-8">--相应头
<meta http-equiv = "X-UA-Compatible" content = "IE=EmulateIE7" /> --兼容性
```

### 非<meta>标签
tilte标签
link标签显示图标
link引入CSS标签
script引入js标签

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
#### div标签

#### img标签
解释器会开一个线程，线程把图片加载出来
一般不用img中的height和width，用css来调整


### 超链接标签(锚标签)<a></a>
什么是超链接
所谓的超链接是指从一个网页指向另一个目标的连接关系，这个目标可以是另一个网页，也可以是相同网页上的不同位置，还可以是一个图片，一个电子邮件地址，一个文件，甚至是一个应用程序。

什么是URL？
URL是统一资源定位器的缩写，也被称为网页地址，是因特网上标准的资源地址。
URL举例
http://www.baidu.com/index.html
http://222.172.123.33/stu/intro.html

URL地址由4部分组成:
第一部分:为协议:http://、ftp:// 等
第二部分:为站点地址:可以是域名或IP地址
第三部分:为页面在站点中的目录:stu
第四部分:为页面名称，例如:index.html
各部分之间用"/"隔开

```html
<a href="" target="_blank">click</a>
```
href属性指定目标网页地址。该地址可以有几种类型:
绝对URL -- 指向另一个站点(例如 href="http://www.baidu.com")
相对URL -- 指向当前站点中确切的路径(href='index.html')
锚 URL -- 指向页面中的锚(href="#top")

href=""如果不写任何值，点击a标签相当于刷新

id相当于标签身份证


### 列表标签
无序列表:
有序列表:
定义列表

无序列表unorder list
```html
<ul>
    <li>111</li>
    <li>222</li>
</ul>
```
有序列表order list
```html
<ol>
    <li>111</li>
    <li>222</li>
    <li>333</li>
</ol>
```

定义列表
```html
<dl>
    <dt>标题</dt> define Title
    <dd>item1</dd> define data
    <dd>item2</dd>
    <dd>item3</dd>
</dl>
```


### table表格标签
table
tr:table row
td:table data
th:table head

```html
<table border="2px">
    <tr>
        <td>语文</td>
        <td>数学</td>
        <td>英语</td>
        <td>音乐</td>
    </tr>
</table>
```

```html
<table border="2px">
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

调整表格的间距:
cellpadding:内容的举例
cellspacing:间距的举例
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

合并表格:
rowspan:
colspan:

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

### form表单标签

功能:表单用于向服务器传输数据，从而实现用户与Web服务器的交互。
表单能够包含input系列标签，比如文本字段、复选框、单选框、提交按钮等等。
表单还可以包含textarea、select、fieldset和label标签。

input中type属性:
  text明文
  password:密文
  checkbox:复选框,需要加value,checked="checked"
  radio:单选框，一般用来互斥,需要name定义一样，需要加value
  hidden:默认值的时候一般用hidden，不需要用户来选，默认的。
  file:选择文件，可以上传

  button:一般和js事件连用，用来绑定事件
  submit:提交数据，修改submit中提交字样，定义value=""，这个value和之前的不一样，并不是一个键值对
input表单必须加name,不加name属性没有意义


form属性:只要form表单的都要有name，不然不能形成键值对
action:放路径，将数据传送给谁
method:get,post HTTP协议中的前端给后端提供数据的方式


```html
</p>用户名:<input type="text" name="username"></p> {username:yuan}
</p>密码:<input type="password" name="pwd"></p> {pwd:123}
```

```html
<p>爱好:写作<input type="checkbox" name="habits" value="writing">
        阅读<input type="checkbox" name="habits" value="reading"></p>

{"habits":["writing","reading"]}
```

在form表单之外写input标签没有任何意义

#### form表单与Django交互
等django学完了再做

select:下拉框,和option连用，size:最大可显示几个,multiple="multiple"表示多选，如果属性名字和属性值相同，直接写一个就行，multiple,默认选择selected='selected'，optgroup:分组，label标签表示分组的名称

textarea

label标签

<label for="username">用户名</label>
<input type="text" name="username" id="username">

fileset标签
<fieldset>
    <legend>登录吧</legend>
    <input type="text">
</fieldset>
