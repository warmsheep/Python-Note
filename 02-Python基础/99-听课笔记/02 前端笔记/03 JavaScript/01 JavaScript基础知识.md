# JavaScript

DOM----document object model
BOM----browser object model

## JS的引入方式
### 1 直接编写
### 2 导入文件
```js
    <script>
        alert('hello yuan')
    </script>
    ### 2 导入文件
```

### 2 导入文件
```js
<script src="hello.js"></script>
```

js是一门相当随便的语言:
## JS的变量、常量和标识符
### 2.1 变量
x=5
y=6
z=x+y

在代数中，我们使用字母（比如 x）来保存值（比如 5）。通过上面的表达式 z=x+y，我们能够计算出 z 的值为 11。在 JavaScript 中，这些字母被称为变量。

那么如何在JS中定义使用变量呢？

* 1、声明变量时不用声明变量类型. 全都使用var关键字;

```js
var a;<br>a=3;
```

* 2、一行可以声明多个变量.并且可以是不同类型

```js
var name="yuan", age=20, job="lecturer";
```

* 3、声明变量时 可以不用var. 如果不用var 那么它是全局变量

* 4、变量命名,首字符只能是字母,下划线,$美元符 三选一，余下的字符可以是下划线、美元符号或任何字母或数字字符且区分大小写，x与X是两个变量　

**命名规范**
* Camel 标记法
首字母是小写的，接下来的字母都以大写字符开头。例如：
var myTestValue = 0, mySecondValue = "hi";
* Pascal 标记法
首字母是大写的，接下来的字母都以大写字符开头。例如：
Var MyTestValue = 0, MySecondValue = "hi";
* 匈牙利类型标记法
在以 Pascal 标记法命名的变量前附加一个小写字母（或小写字母序列），说明该变量的类型。例如，i 表示整数，s 表示字符串，如下所示“
Var iMyTestValue = 0, sMySecondValue = "hi";

什么是强类型，弱类型语言？

python是一门强类型语言，动态语言

什么是动态语言？

如果不加;，以换行符为;

### 2.2 常量和标识符
常量 ：直接在程序中出现的数据值
标识符：
* 1.由不以数字开头的字母、数字、下划线(\_)、美元符号($)组成
* 2.常用于表示函数、变量等的名称
* 3.例如：\_abc,$abc,abc,abc123是标识符，而1abc不是
* 4.JavaScript语言中代表特定含义的词称为保留字，不允许程序再定义为标识符

![js的保留字](https://images2015.cnblogs.com/blog/877318/201610/877318-20161020152532717-389530735.png)

![js定义的函数](https://images2015.cnblogs.com/blog/877318/201610/877318-20161020153916560-1468649784.png)

## JS的数据类型
![js数据类型](https://images2015.cnblogs.com/blog/877318/201610/877318-20161023225846513-154917493.png)

![堆和栈](https://images2015.cnblogs.com/blog/877318/201610/877318-20161023224930873-196677017.png)

* number     -----  数值
* boolean    -----  布尔值
* string     -----  字符串
* undefined  -----  undefined
* null       -----   null  


### 数字类型(Number)
简介
最基本的数据类型
不区分整形数值和浮点型数值
所有的数字都采用64位浮点格式存储，相当于Java和c语言


var num = 10;
var num1 = 10;//表示整数10
var num2 = 1.1;//表示的是浮点数1.1
var num3 = .1;//表示的是0.1
var num4 = 10.0;//整数，解析成10
var num5 = 10.;//小数点后面没有数字，解析成10
var num6 = 3.124e7;//等于31240000，科学计数法

* 不区分整型数值和浮点型数值;
* 所有数字都采用64位浮点格式存储，相当于Java和C语言中的double格式
* 能表示的最大值是±1.7976931348623157 x 10308
* 能表示的最小值是±5 x 10 -324 　


### 字符串(string)

是由Unicode字符、数字、标点符号组成的序列；字符串常量首尾由单引号或双引号括起；JavaScript中没有字符类型；常用特殊字符在字符串中的表达；
字符串中部分特殊字符必须加上右划线\；常用的转义字符 \n:换行 \':单引号 \":双引号 \\:右划线

### 布尔类型(boolean)

Boolean类型仅有两个值：true和false，也代表1和0，实际运算中true=1,false=0
布尔值也可以看作on/off、yes/no、1/0对应true/false
Boolean值主要用于JavaScript的控制语句，例如：


### Null & Undefined类型
#### Undefined类型

Undefined 类型只有一个值，即undefined。

当声明的变量未初始化时，该变量的默认值是 undefined。(声明变量却未赋值)

当函数无明确返回值时，返回的也是值 "undefined";

#### Null类型

另一种只有一个值的类型是 Null，它只有一个专用值 null，即它的字面量。值 undefined 实际上是从值 null 派生来的，因此 ECMAScript 把它们定义为相等的。

尽管这两个值相等，但它们的含义不同。undefined 是声明了变量但未对其初始化时赋予该变量的值，null 则用于表示尚未存在的对象（在讨论 typeof 运算符时，简单地介绍过这一点）。如果函数或方法要返回的是对象，那么找不到该对象时，返回的通常是 null。

var person = new Person();
var person = null;

### 类型转换

JavaScript属于松散类型的程序语言
变量在声明的时候并不需要指定数据类型
变量只有在赋值的时候才会确定数据类型
表达式中包含不同类型数据则在计算过程中会强制进行类别转换


数字 + 字符串：数字转换为字符串
数字 + 布尔值：true转换为1，false转换为0
字符串 + 布尔值：布尔值转换为字符串true或false

#### 强制类型转换函数
* parseInt函数
* parseFloat函数:强制转换成浮点数 parseFloat("6.12") = 6.12;
* eval函数:把字符串转换成表达式

NaN: not a number类型，当涉及数据转换成数字时候，得不到结果会得到这种数字类型,NaN本身是number类型

类型查询函数typeof

typeof(null) object


## JS运算符
* 算术运算符
* 逻辑运算符
* 赋值运算符
* 等性运算符
* 位运算

NaN和谁做比较都是false
只有一种可能是true,!=的情况

## JS控制语句
流程控制语句，if elif... else 出现分支只走一个
while 相当于只走很多次
break continue
### if控制语句
if (表达式) {
    语句1
}else{
    语句2
}

### switch case语句

### for循环控制语句

for (初始化;条件;增量){
    语句

}

### while循环

while (条件) {
    语句1;
    ...
}

### 异常处理
try {
  //这段代码从上往下运行，其中任何一个语句抛出异常改代码块就运行结束

}
catch (e) {
  //如果try代码块中抛出了异常，catch代码块中的代码就会被执行
  // e是一个局部变量，用来指向Error对象或者其他抛出的对象

}
finally{
  //无论try代码是否有异常抛出(甚至是try代码块中有return语句)，finally代码块中始终会被执行
}

主动抛出异常:


## JS对象

![js内置对象分类](https://images2015.cnblogs.com/blog/877318/201610/877318-20161020172116545-1736844688.png)

### String对象
#### 字符串对象的属性和函数
* x.length --获取字符串的长度
* x.substr(start,length) --start表示开始位置，length表示
* x.


### 数组对象
function intsort2(a,b){
    return a-b
}

### Date对象

### Math对象

### 函数对象

function 函数名 (参数){
    函数主体;
    return 返回值  
}

function也可以不加return，默认返回undefined;


## BOM对象
browser object model

### window对象

## 节点查找
document.getElementById()


mouseleave和mouseout区别




## DOM对象
