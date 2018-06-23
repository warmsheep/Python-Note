# CSS知识
1.查找标签(选择器)
2.操作标签(属性操作)

## 引入CSS方式
1.行内式
给标签直接加style属性
```html
<p style="color:red;background-color:green">hello WarmJunee</p>
```

2.嵌入式
只能用于本页面，不能应用于其他的页面
引入数目没有限制
```html
<style>
    p{
    color:green;
    background:yellow;
    }
</style>
```

3.链接式(推荐用这个)
<link rel="stylesheet" href="index.css">
可以用于多个页面，将css格式用于多个页面

4.导入式(了解)
加载顺序:先加载下面的内容，再加载CSS的样式
引入数目是有限制的

```
<style>
    @import "test_css.css"
</style>
```


## 选择器
### 基础选择器
![基础选择器](https://images2015.cnblogs.com/blog/877318/201705/877318-20170517132804978-1482408610.png)

id和class可以同时设置

### 组合选择器

一个块级标签可以嵌套块级和内联标签，但是内联标签不可以嵌套块级标签
例外:p标签不能嵌套任何块级标签

* E,F   多元素选择器，同时匹配所有E元素或F元素，E和F之间用逗号分隔      :div,p { color:#f00; }

* E F   后代元素选择器，匹配所有属于E元素后代的F元素，E和F之间用空格分隔 :li a { font-weight:bold;｝

* E > F   子元素选择器，匹配所有E元素的子元素F            :div > p { color:#f00; }

* E + F   毗邻元素选择器，向下紧挨着，匹配所有紧随E元素之后的同级元素F,最靠近E的F,只能向下找，不会向上找  :div + p { color:#f00; }

* E ~ F   普通兄弟选择器,向下查找同级（以破折号分隔）                 :.div1 ~ p{font-size: 30px; }


### 属性选择器
E:Element(元素)
注意:E和[]之间不能加空格，加了空格相当于后代选择器。

属性可以赋值多个值，不同值用空格分开，如下:
<div po='p1' class='c1 btn'>p1</div>
<div po='p1 p' class='c1 btn'>p1</div>

* E[att]          匹配所有具有att属性的E元素，不考虑它的值。（注意：E在此处可以省略。
                比如“[cheacked]”。以下同。）   p[title] { color:#f00; }

* E[att=val]      匹配所有att属性等于“val”的E元素 ，只适用于属性单值和如果多值，需要全部写入(但是没有意义)  div[class=”error”] { color:#f00; }


* E[att~=val]     匹配所有att属性具有多个空格分隔的值、其中一个值等于“val”的E元素，属性存在多个值，必须加上~，不然无法渲染
                td[class~=”name”] { color:#f00; }

* E[attr^=val]    匹配属性值以指定值开头的每个元素                    
                div[class^="test"]{background:#ffff00;}

* E[attr$=val]    匹配属性值以指定值结尾的每个元素    div[class$="test"]{background:#ffff00;}

* E[attr*=val]    匹配属性值中包含指定值的每个元素，对于属性多个值也适用。    div[class*="test"]{background:#ffff00;}


### 伪类选择器
#### anchor伪类：专用于控制链接的显示效果
hover一定是父类控制子类，没有说兄弟互相控制的

* a:link（没有接触过的链接）,用于定义了链接的常规状态。

* a:hover（鼠标放在链接上的状态）,用于产生视觉效果。

* a:visited（访问过的链接）,用于阅读文章，能清楚的判断已经访问过的链接。

* a:active（在链接上按下鼠标时的状态）,用于表现鼠标按下时的链接状态。

* 伪类选择器 : 伪类指的是标签的不同状态:

           a ==> 点过状态 没有点过的状态 鼠标悬浮状态 激活状态

* a:link {color: #FF0000} /* 未访问的链接 \*/

* a:visited {color: #00FF00} /* 已访问的链接 \*/

* a:hover {color: #FF00FF} /* 鼠标移动到链接上 \*/

* a:active {color: #0000FF} /* 选定的链接 \*/ 格式: 标签:伪类名称{ css代码; }


#### before after伪类选择器
添加内容

:before    p:before       在每个<p>元素之前插入内容     
 :after     p:after        在每个<p>元素之后插入内容     

例：p:before{content:"hello";color:red;display: block;}


### 选择器的优先级

#### css的继承

继承是CSS的一个主要特征，它是依赖于祖先-后代的关系的。继承是一种机制，它允许样式不仅可以应用于某个特定的元素，还可以应用于它的后代。例如一个BODY定义了的颜色值也会应用到段落的文本中。


这段文字都继承了由body {color:red;}样式定义的颜色。然而CSS继承性的权重是非常低的，是比普通元素的权重还要低的0。


#### css的优先级(重点)
所谓CSS优先级，即是指CSS样式在浏览器中被解析的先后顺序。

样式表中的特殊性描述了不同规则的相对权重，它的基本规则是：

1 内联样式表的权值最高           style=""－－－－－－－－－－－－1000；

2 统计选择符中的ID属性个数。      #id －－－－－－－－－－－－－－100

3 统计选择符中的CLASS属性个数。  .class －－－－－－－－－－－－－10

4 统计选择符中的HTML标签名个数。 p －－－－－－－－－－－－－－－－1

按这些规则将数字符串逐位相加，就得到最终的权重，然后在比较取舍时按照从左到右的顺序逐位比较。

**优先级总结**
1、文内的样式优先级为1,0,0,0，所以始终高于外部定义。
2、有!important声明的规则高于一切。

```css
.p2{
    color:red!important;
        }
```
3、如果!important声明冲突，则比较优先权。

4、如果优先权一样，则按照在源码中出现的顺序决定，后来者居上。

5、由继承而得到的样式没有specificity的计算，它低于一切其它规则(比如全局选择符*定义的规则)。

## CSS属性操作

### 文本属性

#### 文本颜色：color
颜色属性被用来设置文字的颜色。

颜色是通过CSS最经常的指定：

十六进制值 - 如: ＃FF0000
一个RGB值 - 如: RGB(255,0,0)
颜色的名称 - 如:  red

百度:颜色代码表
rgba(255,0,0,0.3)
a:代表透明度(0-1),1是纯的颜色
opacity:透明度

```css
p { color: rebeccapurple;  }
```

### 水平对齐方式：text-align
text-align 属性规定元素中的文本的水平对齐方式。

* left     把文本排列到左边。默认值：由浏览器决定。
* right    把文本排列到右边。
* center   把文本排列到中间。
* justify  实现两端对齐文本效果。

#### 文本其他属性
* font-size: 10px;字体大小

* line-height: 200px;   文本行高 通俗的讲，文字高度加上文字上下的空白区域的高度 50%:基于字体大小的百分比, 超出部分:overflow:scroll;(重点)，行高设定，内容超出，直接写下面一行。内容的大小是固定的，行高其余的都是空隙，如果line-height=height，只能写一行，第二行会溢出。

* vertical-align:－4px  设置元素内容的垂直对齐方式 ,只对行内元素有效，对块级元素无效

* text-decoration:none       text-decoration 属性用来设置或删除文本的装饰。主要是用来删除链接的下划线

* font-family: 'Lucida Bright'

* font-weight: lighter/bold/border/

* font-style: oblique

* text-indent: 150px;      首行缩进150px

* letter-spacing: 10px;  字母间距

* word-spacing: 20px;  单词间距

* text-transform: capitalize/uppercase/lowercase ; 文本转换，用于所有字句变成大写或小写字母，或每个单词的首字母大写

### 背景属性

顺序都可以颠倒的

* background-color
* background-image
* background-repeat
* background-position


background-color: cornflowerblue

background-image: url('1.jpg');

background-repeat: no-repeat;(repeat:平铺满)

background-position: right top（20px 20px）;



* background:#ffffff url('1.png') no-repeat right top;

100px

#### 边框属性

* border-width
* border-style (required)
* border-color

也可以设置只有某个边框

border-style: solid;

border-color: chartreuse;

border-width: 20px;

border-bottom
border-right

#### 列表属性

list-style-type     设置列表项标志的类型。circle square none
list-style-image    将图象设置为列表项标志。
list-style-position 设置列表中列表项标志的位置。

list-style          简写属性。用于把所有用于列表的属性设置于一个声明中

使用图像来替换列表项的标记:
```css
ul {
     list-style-image: url('');
            }
```

### display属性
* none
* block
* inline:不能做长宽
* inline-block:能设置长款

#### none(隐藏某标签)
```css
p{display:none;}
```
**注意与visibility:hidden的区别：**

visibility:hidden可以隐藏某个元素，但隐藏的元素仍需占用与未隐藏之前一样的空间。也就是说，该元素虽然被隐藏了，但仍然会影响布局。

display:none可以隐藏某个元素，且隐藏的元素不会占用任何空间。也就是说，该元素不但被隐藏了，而且该元素原本占用的空间也会从页面布局中消失。

#### block(内联标签设置为块级标签)

span {display:block;}
注意：一个内联元素设置为display:block是不允许有它内部的嵌套块元素。　

#### inline(块级标签设置为内联标签)

li {display:inline;}

#### inline-block

display:inline-block可做列表布局，其中的类似于图片间的间隙小bug可以通过如下设置解决：

inline-block的块之间默认会有缝隙，缝隙如果不想要的话，先把他们放在大的盒子里，然后设置word-spacing为负数就行，但是大的盒子也应该是inline-block,也可以用margin来设置;
直接用*{margin:0,padding:0}能设置成功。
```css
#outer{
          border: 3px dashed;
          word-spacing: -5px;
        }
```

同样的属性可以放在一个设置中


float也可以设置长宽，让内联变成块级标签，让块级变成内联块标签


### 外边距(margine)和内边距(padding)
#### 盒子模型
![盒子模型](https://images2015.cnblogs.com/blog/877318/201610/877318-20161020102031154-222250498.png)

* margin:            用于控制元素与元素之间的距离；margin的最基本用途就是控制元素周围空间的间隔，从视觉角度上达到相互隔开的目的。
margin上下边距冲突取较大的外边距，但是左右相遇不会融合
* padding:           用于控制内容与边框之间的距离；   
* Border(边框):     围绕在内边距和内容外的边框。
* Content(内容):   盒子的内容，显示文本和图像。

#### margine(外边距)

单边外边距属性：
* margin-top:100px;
* margin-bottom:100px;
* margin-right:50px;
* margin-left:50px;

简写属性　
* margin:10px 20px 20px 10px；

        上边距为10px
        右边距为20px
        下边距为20px
        左边距为10px

* margin:10px 20px 10px;

        上边距为10px
        左右边距为20px
        下边距为10px

* margin:10px 20px;

        上下边距为10px
        左右边距为20px

* margin:25px;

        所有的4个边距都是25px

居中应用
* margin: 0 auto;

#### padding(内边距)

单独使用填充属性可以改变上下左右的填充。缩写填充属性也可以使用，一旦改变一切都改变。

设置同margine；

**思考1:body的外边距**
边框在默认情况下会定位于浏览器窗口的左上角，但是并没有紧贴着浏览器的窗口的边框，这是因为body本身也是一个盒子（外层还有html），在默认情况下，   body距离html会有若干像素的margin，具体数值因各个浏览器不尽相同，所以body中的盒子不会紧贴浏览器窗口的边框了，为了验证这一点，加上：

body{
    border: 1px solid;
    background-color: cadetblue;
}


解决方法：
body{
    margin: 0;
}

**思考2：margin collapse（边界塌陷或者说边界重叠）**
上述情况只针对上下，对左右没有影响。

1、兄弟div：
上面div的margin-bottom和下面div的margin-top会塌陷，也就是会取上下两者margin里最大值作为显示值

2、父子div：
如果父级div中没有border，padding，inlinecontent，子级div的margin会一直向上找，直到找到某个标签包括border，padding，inline content中的其中一个，然后按此div 进行margin；

解决方法：
1.给父盒子加overflow: hidden;　   
2.给父盒子加border或者padding，但是会影响到原始的布局
3.给父盒子加属性:inlinecontent:"";

将一个盒子调到中间来，用margin和padding来设置


margin:改变位置，不影响元素大小
padding:会影响元素大小

### float属性
#### 基本浮动规则
先来了解一下block元素和inline元素在文档流中的排列方式。

block元素通常被现实为独立的一块，独占一行，多个block元素会各自新起一行，默认block元素宽度自动填满其父元素宽度。block元素可以设置width、height、margin、padding属性；

inline元素不会独占一行，多个相邻的行内元素会排列在同一行里，直到一行排列不下，才会新换一行，其宽度随元素的内容而变化。inline元素设置width、height属性无效

* 常见的块级元素有 div、form、table、p、pre、h1～h5、dl、ol、ul 等。
* 常见的内联元素有span、a、strong、em、label、input、select、textarea、img、br等

所谓的文档流，指的是元素排版布局过程中，元素会自动从左往右，从上往下的流式排列。

脱离文档流，也就是将元素从普通的布局排版中拿走，其他盒子在定位的时候，会当做脱离文档流的元素不存在而进行定位。

假如某个div元素A是浮动的，如果A元素上一个元素也是浮动的，那么A元素会跟随在上一个元素的后边(如果一行放不下这两个元素，那么A元素会被挤到下一行)；如果A元素上一个元素是标准流中的元素，那么A的相对垂直位置不会改变，也就是说A的顶部总是和上一个元素的底部对齐。此外，浮动的框之后的block元素元素会认为这个框不存在，但其中的文本依然会为这个元素让出位置。 浮动的框之后的inline元素，会为这个框空出位置，然后按顺序排列。

浮动元素到底往哪里浮，取决于上一个元素按什么排，如果在文档流，保持垂直，如果浮动，则贴着走。

float:
  浮动元素会判断上一个元素是否浮动，如果浮动，紧贴上一个浮动元素，否则，在上一个元素的垂直下方

#### 非完全脱离文档流

左右结构div盒子重叠现象，一般是由于相邻两个DIV一个使用浮动一个没有使用浮动。一个使用浮动一个没有导致DIV不是在同个“平面”上，但内容不会造成覆盖现象，只有DIV形成覆盖现象。



clear清除浮动，清楚的是自己的周围的浮动元素，影响的是自己
左漂left,clear:left,
右漂right,clear:right
float不会覆盖文本元素，

### 塌陷的解决办法
* 1.
* 2.
* 3.
* 4.


### position(定位)

#### 1 static
static 默认值，无定位，不能当作绝对定位的参照物，并且设置标签对象的left、top等值是不起作用的的。

#### 2  position: relative／absolute
**relative: 相对定位。**
相对定位是相对于该元素在文档流中的原始位置，即以自己原始位置为参照物。有趣的是，即使设定了元素的相对定位以及偏移值，元素还占有着原来的位置，即占据文档流空间。对象遵循正常文档流，但将依据top，right，bottom，left等属性在正常文档流中偏移位置。而其层叠通过z-index属性定义。
1.参照物是钙元素在文档流中的原始位置
2.元素不脱离文档流(之前的空间位置依然存在)

注意：position：relative的一个主要用法：方便绝对定位元素找到参照物。

**absolute: 绝对定位。**
定义：设置为绝对定位的元素框从文档流完全删除，并相对于最近的已定位祖先元素定位，如果元素没有已定位的祖先元素，那么它的位置相对于最初的包含块（即body元素）。元素原先在正常文档流中所占的空间会关闭，就好像该元素原来不存在一样。元素定位后生成一个块级框，而不论原来它在正常流中生成何种类型的框。

重点：如果父级设置了position属性，例如position:relative;，那么子元素就会以父级的左上角为原始点进行定位。这样能很好的解决自适应网站的标签偏离问题，即父级为自适应的，那我子元素就设置position:absolute;父元素设置position:relative;，然后Top、Right、Bottom、Left用百分比宽度表示。

另外，对象脱离正常文档流，使用top，right，bottom，left等属性进行绝对定位。而其层叠通过z-index属性定义。
1.absolute会脱离文档流
2.父元素:position:relative
  子元素:position:absolute;


#### 3  position:fixed

fixed：对象脱离正常文档流，使用top，right，bottom，left等属性以窗口为参考点进行定位，当出现滚动条时，对象不会随着滚动。而其层叠通过z-index属性 定义。 注意点： 一个元素若设置了 position:absolute | fixed; 则该元素就不能设置float。这 是一个常识性的知识点，因为这是两个不同的流，一个是浮动流，另一个是“定位流”。但是 relative 却可以。因为它原本所占的空间仍然占据文档流。

在理论上，被设置为fixed的元素会被定位于浏览器窗口的一个指定坐标，不论窗口是否滚动，它都会固定在这个位置。

脱离文档流:float;position:absolute/fixed
