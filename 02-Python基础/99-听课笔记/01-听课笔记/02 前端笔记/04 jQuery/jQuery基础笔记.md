# jQuery基础知识

## 一 jQuery是什么？

<1> jQuery由美国人John Resig创建，至今已吸引了来自世界各地的众多 javascript高手加入其team。

<2> jQuery是继prototype之后又一个优秀的Javascript框架。其宗旨是——WRITE LESS,DO MORE!

<3> 它是轻量级的js库(压缩后只有21k) ，这是其它的js库所不及的，它兼容CSS3，还兼容各种浏览器

<4> jQuery是一个快速的，简洁的javaScript库，使用户能更方便地处理HTMLdocuments、events、实现动画效果，并且方便地为网站提供AJAX交互。

<5> jQuery还有一个比较大的优势是，它的文档说明很全，而且各种应用也说得很详细，同时还有许多成熟的插件可供选择


## 二 什么是jQuery对象？

jQuery 对象就是通过jQuery包装DOM对象后产生的对象。jQuery 对象是 jQuery 独有的. 如果一个对象是 jQuery 对象, 那么它就可以使用 jQuery 里的方法: $(“#test”).html();$也可以换成jQuery

虽然jQuery对象是包装DOM对象后产生的，但是jQuery无法使用DOM对象的任何方法，同理DOM对象也不能使用jQuery里的方法.乱使用会报错



### jQuery对象和DOM对象的转换

```js
$("#test").html()   //jQuery对象（“#test”).html
//意思是指：获取ID为test的元素内的html代码。其中html()是jQuery里的方法 ，下面用DOM对象实现同样的方法
document.getElementById("test").innerHTML;//DOM对象
```

**约定：** 如果获取的是 jQuery 对象, 那么要在变量前面加上$.

```js
var $variable = jQuery 对象
var variable = DOM 对象
```

### 将jQuery对象转换dom对象
```js
$variable[0]：jquery对象转为dom对象      
//例如
$("#msg").html();
$("#msg")[0].innerHTML
```

jquery的基础语法：**$(selector).action()**

js下: cloneNode
jQuery: clone()

## 三 寻找元素(选择器和筛选器)
### 3.1   选择器
#### 3.1.1 基本选择器
* 通配符选择器：$("\*")
* ID选择器：$("#id")
* class选择器：$(".class")
* 元素选择器：$("element")
* 并集选择器：$("selector1,selector2,selectorN")

#### 3.1.2 层级选择器    
* 后代选择器：$("ancestor descendant")  
* 子代选择器：$("parent>child")   
* 毗邻选择器：$("prev+next")  
* 兄弟选择器：$("prev~siblings")

#### 3.1.3 基本筛选器  
    
* 第一个li：$("li:first")  
* 索引为2的li：$("li:eq(2)")  
* 索引为偶数：$("li:even")
* 索引大于1的：$("li:gt(1)")

#### 3.1.4 属性选择器    
* id属性等于div1的标签：$('[id="div1"]')   
* alex属性等于sb的标签：$('["alex="sb"][id]')

#### 3.1.5 表单选择器     
* type为text的input标签：$("[type='text']")
* 可以简写为：$(":text")         
**注意** 该方法只适用于input标签: $("input:checked")

##### 实例之左侧菜单
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>left_menu</title>

    <style>
          .menu{
              height: 500px;
              width: 30%;
              background-color: gainsboro;
              float: left;
          }
          .content{
              height: 500px;
              width: 70%;
              background-color: rebeccapurple;
              float: left;
          }
         .title{
             line-height: 50px;
             background-color: #425a66;
             color: forestgreen;}


         .hide{
             display: none;
         }


    </style>
</head>
<body>

<div class="outer">
    <div class="menu">
        <div class="item">
            <div class="title">菜单一</div>
            <div class="con">
                <div>111</div>
                <div>111</div>
                <div>111</div>
            </div>
        </div>
        <div class="item">
            <div class="title">菜单二</div>
            <div class="con hide">
                <div>111</div>
                <div>111</div>
                <div>111</div>
            </div>
        </div>
        <div class="item">
            <div class="title">菜单三</div>
            <div class="con hide">
                <div>111</div>
                <div>111</div>
                <div>111</div>
            </div>
        </div>

    </div>
    <div class="content"></div>

</div>
<script src="jquery-3.2.1.js"></script>
<script>
           $(".item .title").click(function () {
                $(this).next().removeClass("hide").parent().siblings().children(".con").addClass("hide");

//                $(this).next().removeClass("hide");
//                $(this).parent().siblings().children(".con").addClass("hide");
           })
</script>
</body>
</html>
```

##### 实例之tab切换
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>tab</title>
    <script>
           function tab(self){
               var index=$(self).attr("xxx");
               $("#"+index).removeClass("hide").siblings().addClass("hide");
               $(self).addClass("current").siblings().removeClass("current");

           }
    </script>
    <style>
        *{
            margin: 0px;
            padding: 0px;
        }
        .tab_outer{
            margin: 0px auto;
            width: 60%;
        }
        .menu{
            background-color: #cccccc;
            /*border: 1px solid red;*/
            line-height: 40px;
        }
        .menu li{
            display: inline-block;
        }
        .menu a{
            border-right: 1px solid red;
            padding: 11px;
        }
        .content{
            background-color: tan;
            border: 1px solid green;
            height: 300px;
        }
        .hide{
            display: none;
        }

        .current{
            background-color: darkgray;
            color: yellow;
            border-top: solid 2px rebeccapurple;
        }
    </style>
</head>
<body>
      <div class="tab_outer">
          <ul class="menu">
              <li xxx="c1" class="current" onclick="tab(this);">菜单一</li>
              <li xxx="c2" onclick="tab(this);">菜单二</li>
              <li xxx="c3" onclick="tab(this);">菜单三</li>
          </ul>
          <div class="content">
              <div id="c1">内容一</div>
              <div id="c2" class="hide">内容二</div>
              <div id="c3" class="hide">内容三</div>
          </div>

      </div>
</body>
</html>
```

### 3.2 筛选器
####  3.2.1  过滤筛选器     
* 索引为2的li标签：$("li").eq(2)  
* 第一个li标签：$("li").first()  
* li标签是否含有test属性：$("ul li").hasclass("test")

####  3.2.2  查找筛选器

* div标签下class为test的子代标签：$("div").children(".test")
* div下查找是否有class为test属性的标签：$("div").find(".test")  
* class=test的元素的紧邻同辈元素 ：$(".test").next()    
* 当前元素之后所有的同辈元素：$(".test").nextAll()    
* 查找当前元素之后所有的同辈元素，直到遇到匹配的那个元素为止（开区间）：$(".test").nextUntil()

* div标签紧邻的钱一个同辈元素：$("div").prev()  
* 查找当前元素之前所有的同辈元素：$("div").prevAll()  
* 查找当前元素之前所有的同辈元素，直到遇到匹配的那个元素为止。：$("div").prevUntil()                        
* 取得一个包含着所有匹配元素的唯一父元素的元素集合：$(".test").parent()  
* 取得一个包含着所有匹配元素的祖先元素的元素集合（不包含根元素）：$(".test").parents()  
* 查找当前元素的所有的父辈元素，直到遇到匹配的那个元素为止：$(".test").parentUntil()
* 取得一个包含匹配的元素集合中每一个元素的所有唯一同辈元素的元素集合：$("div").siblings()

## 四 操作元素(属性，css，文档处理)
### 4.1 属性操作
#### 属性
* $("").attr();一般是自定义的属性
* $("").removeAttr();
* $("").prop();一般是元素固有的属性
* $("").removeProp();

#### CSS类
* $("").addClass(class|fn);增加某个class属性
* $("").removeClass([class|fn]);删除某个class属性

#### HTML代码/文本/值
* $("").html([val|fn])
* $("").text([val|fn])
* $("").val([val|fn|arr])

#### 设置CSS属性
* $("").css("color","red")

#### 注意：
```html
<input id="chk1" type="checkbox" />是否可见
<input id="chk2" type="checkbox" checked="checked" />是否可见

<script>
console.log($("#chk1").prop("checked"));//false
console.log($("#chk2").prop("checked"));//true
console.log($("#chk1").attr("checked"));//undefined手动选中的时候attr()获得到没有意义的undefined
console.log($("#chk2").attr("checked"));//checked
</script>
```
* 对于HTML元素本身就带有的固有属性，在处理时，使用prop方法。
* 对于HTML元素我们自己自定义的DOM属性，在处理时，使用attr方法。
* 像checkbox，radio和select这样的元素，选中属性对应“checked”和“selected”，这些也属于固有属性，因此需要使用prop方法去操作才能获得正确的结果。

##### 实例之全反选
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="jquery-1.11.3.min.js"></script>
    <script>

             function selectall(){

                 $("table :checkbox").prop("checked",true)
             }
             function cancel(){

                 $("table :checkbox").prop("checked",false)
             }

             function reverse(){


                 //                 var idlist=$("table :checkbox")
//                 for(var i=0;i<idlist.length;i++){
//                     var element=idlist[i];
//
//                     var ischecked=$(element).prop("checked")
//                     if (ischecked){
//                         $(element).prop("checked",false)
//                     }
//                     else {
//                         $(element).prop("checked",true)
//                     }
//
//                 }
//    jquery循环的两种方式
                 //方式一
//                 li=[10,20,30,40]
//                 dic={name:"yuan",sex:"male"}
//                 $.each(li,function(i,x){
//                     console.log(i,x)
//                 })

                 //方式二
//                    $("tr").each(function(){
//                        console.log($(this).html())
//                    })



                 $("table :checkbox").each(function(){

                     $(this).prop("checked",!$(this).prop("checked"));

//                     if ($(this).prop("checked")){
//                         $(this).prop("checked",false)
//                     }
//                     else {
//                         $(this).prop("checked",true)
//                     }

                     // 思考:如果用attr方法可以实现吗?


                 });
             }

    </script>
</head>
<body>

     <button onclick="selectall();">全选</button>
     <button onclick="cancel();">取消</button>
     <button onclick="reverse();">反选</button>

     <table border="1">
         <tr>
             <td><input type="checkbox"></td>
             <td>111</td>
         </tr>
         <tr>
             <td><input type="checkbox"></td>
             <td>222</td>
         </tr>
         <tr>
             <td><input type="checkbox"></td>
             <td>333</td>
         </tr>
         <tr>
             <td><input type="checkbox"></td>
             <td>444</td>
         </tr>
     </table>
</body>
</html>
```


##### 实例之模态对话框
```htm
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .back{
            background-color: rebeccapurple;
            height: 2000px;
        }

        .shade{
            position: fixed;
            top: 0;
            bottom: 0;
            left:0;
            right: 0;
            background-color: coral;
            opacity: 0.4;
        }

        .hide{
            display: none;
        }

        .models{
            position: fixed;
            top: 50%;
            left: 50%;
            margin-left: -100px;
            margin-top: -100px;
            height: 200px;
            width: 200px;
            background-color: gold;

        }
    </style>
</head>
<body>
<div class="back">
    <input id="ID1" type="button" value="click" onclick="action1(this)">
</div>

<div class="shade hide"></div>
<div class="models hide">
    <input id="ID2" type="button" value="cancel" onclick="action2(this)">
</div>


<script src="jquery-1.11.3.min.js"></script>
<script>

    function action1(self){
        $(self).parent().siblings().removeClass("hide");

    }
    function action2(self){
        //$(self).parent().parent().children(".models,.shade").addClass("hide")

        $(self).parent().addClass("hide").prev().addClass("hide")

    }
</script>
</body>
</html>
```

### 4.2 文档处理
#### 创建一个标签对象
* $("<p>")
* $("<p></p>")

#### 内部插入
* $("").append(content|fn)      ----->$("p").append("<b>Hello</b>");
* $("").appendTo(content)       ----->$("p").appendTo("div");
* $("").prepend(content|fn)     ----->$("p").prepend("<b>Hello</b>");
* $("").prependTo(content)      ----->$("p").prependTo("#foo");

#### 外部插入
* $("").after(content|fn)       ----->$("p").after("<b>Hello</b>");
* $("").before(content|fn)      ----->$("p").before("<b>Hello</b>");
* $("").insertAfter(content)    ----->$("p").insertAfter("#foo");
* $("").insertBefore(content)   ----->$("p").insertBefore("#foo");


#### 替换
* $("").replaceWith(content|fn) ----->$("p").replaceWith("<b>Paragraph. </b>");

#### 删除
* $("").empty()  
* $("").remove([expr])

#### 复制
* $("").clone([Even[,deepEven]])


##### 实例之复制样式条

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

</head>
<body>
            <div class="outer">
                <div class="item">
                        <input type="button" value="+" onclick="add(this);">
                        <input type="text">
                </div>
            </div>

<script src="jquery-1.11.3.min.js"></script>
    <script>
            //var $clone_obj=$(self).parent().clone();  // $clone_obj放在这个位置可以吗?
            function add(self){
                // 注意:if var $clone_obj=$(".outer .item").clone();会一遍二,二变四的增加
                 var $clone_obj=$(self).parent().clone();
                 $clone_obj.children(":button").val("-").attr("onclick","removed(this)");
                 $(self).parent().parent().append($clone_obj);
            }
           function removed(self){

               $(self).parent().remove()

           }

    </script>
</body>
</html>
```

### 4.3 css操作
#### CSS
* $("").css(name|pro|[,val|fn])

#### 位置
* $("").offset([coordinates])
* $("").position()
* $("").scrollTop([val])
* $("").scrollLeft([val])

#### 尺寸
* $("").height([val|fn])
* $("").width([val|fn])
* $("").innerHeight()
* $("").innerWidth()
* $("").outerHeight([soptions])
* $("").outerWidth([options])

##### 实例返回顶部
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="js/jquery-2.2.3.js"></script>
    <script>


          window.onscroll=function(){

              var current=$(window).scrollTop();
              console.log(current)
              if (current>100){

                  $(".returnTop").removeClass("hide")
              }
              else {
              $(".returnTop").addClass("hide")
          }
          }


           function returnTop(){
//               $(".div1").scrollTop(0);

               $(window).scrollTop(0)
           }




    </script>
    <style>
        body{
            margin: 0px;
        }
        .returnTop{
            height: 60px;
            width: 100px;
            background-color: darkgray;
            position: fixed;
            right: 0;
            bottom: 0;
            color: greenyellow;
            line-height: 60px;
            text-align: center;
        }
        .div1{
            background-color: orchid;
            font-size: 5px;
            overflow: auto;
            width: 500px;
        }
        .div2{
            background-color: darkcyan;
        }
        .div3{
            background-color: aqua;
        }
        .div{
            height: 300px;
        }
        .hide{
            display: none;
        }
    </style>
</head>
<body>
     <div class="div1 div">
         <p>hello</p>
         <p>hello</p>
         <p>hello</p>
         <p>hello</p>
         <p>hello</p>
         <p>hello</p>
         <p>hello</p>
         <p>hello</p>
         <p>hello</p>
         <p>hello</p>
         <p>hello</p>
         <p>hello</p>
         <p>hello</p>
         <p>hello</p>
         <p>hello</p>
         <p>hello</p>
         <p>hello</p>
         <p>hello</p>

     </div>
     <div class="div2 div"></div>
     <div class="div3 div"></div>
     <div class="returnTop hide" onclick="returnTop();">返回顶部</div>
</body>
</html>
```

## 五 事件
### 页面载入
* ready(fn)  //当DOM载入就绪可以查询及操纵时绑定一个要执行的函数。
* $(document).ready(function(){}) -----------> $(function(){})

### 事件处理
* $("").on(eve,[selector],[data],fn)  // 在选择元素上绑定一个或多个事件的事件处理函数。
  * .on的selector参数是筛选出调用.on方法的dom元素的指定子元素，如：
  ```js
  $('ul').on('click', 'li', function(){console.log('click');})
  //就是筛选出ul下的li给其绑定
  ```
  * click事件；
  * [selector]参数的好处:
      好处在于.on方法为动态添加的元素也能绑上指定事件；如：
  ```js
      //$('ul li').on('click', function(){console.log('click');})的绑定方式和
      //$('ul li').bind('click', function(){console.log('click');})一样；我通过js给ul添加了一个
      //li：$('ul').append('<li>js new li<li>')；这个新加的li是不会被绑上click事件的

      //但是用$('ul').on('click', 'li', function(){console.log('click');}方式绑定，然后动态添加
      //li:$('ul').append('<li>js new li<li>');这个新生成的li被绑上了click事件
  ```
  * [data]参数的调用:
  ```js
           function myHandler(event) {
              alert(event.data.foo);
              }
           $("li").on("click", {foo: "bar"}, myHandler)
  ```

##### 实例之面板拖动
```js
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div style="border: 1px solid #ddd;width: 600px;position: absolute;">
        <div id="title" style="background-color: black;height: 40px;color: white;">
            标题
        </div>
        <div style="height: 300px;">
            内容
        </div>
    </div>
<script type="text/javascript" src="jquery-2.2.3.js"></script>
<script>
    $(function(){
        // 页面加载完成之后自动执行
        $('#title').mouseover(function(){
            $(this).css('cursor','move');
        }).mousedown(function(e){
            //console.log($(this).offset());
            var _event = e || window.event;
            // 原始鼠标横纵坐标位置
            var ord_x = _event.clientX;
            var ord_y = _event.clientY;

            var parent_left = $(this).parent().offset().left;
            var parent_top = $(this).parent().offset().top;

            $(this).bind('mousemove', function(e){
                var _new_event = e || window.event;
                var new_x = _new_event.clientX;
                var new_y = _new_event.clientY;

                var x = parent_left + (new_x - ord_x);
                var y = parent_top + (new_y - ord_y);

                $(this).parent().css('left',x+'px');
                $(this).parent().css('top',y+'px');

            })
        }).mouseup(function(){
            $(this).unbind('mousemove');
        });
    })
</script>
</body>
</html>
```
##### 实例之放大镜

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>bigger</title>
    <style>
        *{
            margin: 0;
            padding:0;
        }
        .outer{
            height: 350px;
            width: 350px;
            border: dashed 5px cornflowerblue;
        }
        .outer .small_box{
            position: relative;
        }
        .outer .small_box .float{
            height: 175px;
            width: 175px;
            background-color: darkgray;
            opacity: 0.4;
            fill-opacity: 0.4;
            position: absolute;
            display: none;

        }

        .outer .big_box{
            height: 400px;
            width: 400px;
            overflow: hidden;
            position:absolute;
            left: 360px;
            top: 0px;
            z-index: 1;
            border: 5px solid rebeccapurple;
            display: none;


        }
        .outer .big_box img{
            position: absolute;
            z-index: 5;
        }


    </style>
</head>
<body>

        <div class="outer">
            <div class="small_box">
                <div class="float"></div>
                <img src="small.jpg">

            </div>
            <div class="big_box">
                <img src="big.jpg">
            </div>

        </div>


<script src="jquery-2.1.4.min.js"></script>
<script>

    $(function(){

          $(".small_box").mouseover(function(){

              $(".float").css("display","block");
              $(".big_box").css("display","block")

          });
          $(".small_box").mouseout(function(){

              $(".float").css("display","none");
              $(".big_box").css("display","none")

          });

          $(".small_box").mousemove(function(e){

              var _event=e || window.event;

              var float_width=$(".float").width();
              var float_height=$(".float").height();

              console.log(float_height,float_width);

              var float_height_half=float_height/2;
              var float_width_half=float_width/2;
              console.log(float_height_half,float_width_half);


               var small_box_width=$(".small_box").height();
               var small_box_height=$(".small_box").width();



//  鼠标点距离左边界的长度与float应该与左边界的距离差半个float的width,height同理
              var mouse_left=_event.clientX-float_width_half;
              var mouse_top=_event.clientY-float_height_half;

              if(mouse_left<0){
                  mouse_left=0
              }else if (mouse_left>small_box_width-float_width){
                  mouse_left=small_box_width-float_width
              }


              if(mouse_top<0){
                  mouse_top=0
              }else if (mouse_top>small_box_height-float_height){
                  mouse_top=small_box_height-float_height
              }

               $(".float").css("left",mouse_left+"px");
               $(".float").css("top",mouse_top+"px")

               var percentX=($(".big_box img").width()-$(".big_box").width())/ (small_box_width-float_width);
               var percentY=($(".big_box img").height()-$(".big_box").height())/(small_box_height-float_height);

              console.log(percentX,percentY)

               $(".big_box img").css("left", -percentX*mouse_left+"px")
               $(".big_box img").css("top", -percentY*mouse_top+"px")
          })
    })


</script>
</body>
</html>
```

## 六 动画效果

##### 显示隐藏
```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="jquery-2.1.4.min.js"></script>
    <script>

$(document).ready(function() {
    $("#hide").click(function () {
        $("p").hide(1000);
    });
    $("#show").click(function () {
        $("p").show(1000);
    });

//用于切换被选元素的 hide() 与 show() 方法。
    $("#toggle").click(function () {
        $("p").toggle();
    });
})

    </script>
    <link type="text/css" rel="stylesheet" href="style.css">
</head>
<body>


    <p>hello</p>
    <button id="hide">隐藏</button>
    <button id="show">显示</button>
    <button id="toggle">切换</button>

</body>
</html>
```
##### 滑动
```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="jquery-2.1.4.min.js"></script>
    <script>
    $(document).ready(function(){
     $("#slideDown").click(function(){
         $("#content").slideDown(1000);
     });
      $("#slideUp").click(function(){
         $("#content").slideUp(1000);
     });
      $("#slideToggle").click(function(){
         $("#content").slideToggle(1000);
     })
  });
    </script>
    <style>

        #content{
            text-align: center;
            background-color: lightblue;
            border:solid 1px red;
            display: none;
            padding: 50px;
        }
    </style>
</head>
<body>

    <div id="slideDown">出现</div>
    <div id="slideUp">隐藏</div>
    <div id="slideToggle">toggle</div>

    <div id="content">helloworld</div>

</body>
</html>
```
##### 淡入淡出
```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="jquery-2.1.4.min.js"></script>
    <script>
    $(document).ready(function(){
   $("#in").click(function(){
       $("#id1").fadeIn(1000);


   });
    $("#out").click(function(){
       $("#id1").fadeOut(1000);

   });
    $("#toggle").click(function(){
       $("#id1").fadeToggle(1000);


   });
    $("#fadeto").click(function(){
       $("#id1").fadeTo(1000,0.4);

   });
});



    </script>

</head>
<body>
      <button id="in">fadein</button>
      <button id="out">fadeout</button>
      <button id="toggle">fadetoggle</button>
      <button id="fadeto">fadeto</button>

      <div id="id1" style="display:none; width: 80px;height: 80px;background-color: blueviolet"></div>

</body>
</html>
```
##### 回调函数
```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="jquery-2.1.4.min.js"></script>

</head>
<body>
  <button>hide</button>
  <p>helloworld helloworld helloworld</p>



 <script>
   $("button").click(function(){
       $("p").hide(1000,function(){
           alert($(this).html())
       })

   })
    </script>
</body>
</html>
```
## 七 扩展方法 (插件机制)

### 一 用JQuery写插件时，最核心的方两个方法
* $.extend(object)      //为JQuery 添加一个静态方法。
* $.fn.extend(object)   //为JQuery实例添加一个方法。

```js
<script>
    jQuery.extend({
          min: function(a, b) { return a < b ? a : b; },
          max: function(a, b) { return a > b ? a : b; }
        });
    console.log($.min(3,4));

//-----------------------------------------------------------------------
$.fn.extend({
    "print":function(){
        for (var i=0;i<this.length;i++){
            console.log($(this)[i].innerHTML)
        }

    }
});

$("p").print();
</script>
```

### 二 定义作用域
定义一个JQuery插件，首先要把这个插件的代码放在一个不受外界干扰的地方。如果用专业些的话来说就是要为这个插件定义私有作用域。外部的代码不能直接访问插件内部的代码。插件内部的代码不污染全局变量。在一定的作用上解耦了插件与运行环境的依赖。

```js
(function(a,b){return a+b})(3,5)

       (function ($) { })(jQuery);
//相当于
        var fn = function ($) { };
        fn(jQuery);
```

### 三 默认参数
定义了jQuery插件之后，如果希望某些参数具有默认值，那么可以以这种方式来指定。
```js
//step01 定义JQuery的作用域
(function ($) {
    //step03-a 插件的默认值属性
    var defaults = {
        prevId: 'prevBtn',
        prevText: 'Previous',
        nextId: 'nextBtn',
        nextText: 'Next'
        //……
    };
    //step06-a 在插件里定义方法
    var showLink = function (obj) {
        $(obj).append(function () { return "(" + $(obj).attr("href") + ")" });
    }

    //step02 插件的扩展方法名称
    $.fn.easySlider = function (options) {
        //step03-b 合并用户自定义属性，默认属性
        var options = $.extend(defaults, options);
        //step4 支持JQuery选择器
        //step5 支持链式调用
        return this.each(function () {
            //step06-b 在插件里定义方法
            showLink(this);
        });
    }
})(jQuery);
```

##### 实例之注册验证
```js
<form class="Form">

    <p><input class="v1" type="text" name="username" mark="用户名"></p>
    <p><input class="v1" type="text" name="email" mark="邮箱"></p>
    <p><input class="v1" type="submit" value="submit"  onclick="return validate()"></p>

</form>

<script src="jquery-3.1.1.js"></script>
<script>
    // 注意:
    // DOM对象--->jquery对象    $(DOM)
    // jquery对象--->DOM对象    $("")[0]

    //---------------------------------------------------------


    // DOM绑定版本
    function validate(){

        flag=true;

        $("Form .v1").each(function(){
            $(this).next("span").remove();// 防止对此点击按钮产生多个span标签
              var value=$(this).val();
            if (value.trim().length==0){
                 var mark=$(this).attr("mark");
                 var ele=document.createElement("span");
                 ele.innerHTML=mark+"不能为空!";
                 $(this).after(ele);
                 $(ele).prop("class","error");// DOM对象转换为jquery对象
                 flag=false;
                 //  return false-------->引出$.each的return false注意点
            }


        });

        return flag
    }
                   //---------------------------------------------------------
//---------------------------------------------------------
                   //---------------------------------------------------------



        function f(){

        for(var i=0;i<4;i++){

            if (i==2){
                return
            }
            console.log(i)
        }

    }
    f();  // 这个例子大家应该不会有问题吧!!!
//------------------------------------------
    li=[11,22,33,44];
    $.each(li,function(i,v){

        if (v==33){
                return ;   //  ===试一试 return false会怎样?
            }
            console.log(v)
    });

//------------------------------------------

    //  $.MyEach(obj,function(i,v){}):
         for(var i in obj){

             func(i,obj[i]) ; //  i就是索引,v就是对应值
             // {}:我们写的大括号的内容就是func的执行语句;
         }

    // 大家再考虑: function里的return只是结束了当前的函数,并不会影响后面函数的执行

    //本来这样没问题,但因为我们的需求里有很多这样的情况:我们不管循环到第几个函数时,一旦return了,
    //希望后面的函数也不再执行了!基于此,jquery在$.each里又加了一步:
         for(var i in obj){

             ret=func(i,obj[i]) ;
             if(ret==false){
                 return ;
             }

         }
    // 这样就很灵活了:
    // <1>如果你想return后下面循环函数继续执行,那么就直接写return或return true
    // <2>如果你不想return后下面循环函数继续执行,那么就直接写return false


// ---------------------------------------------------------------------
   // 说了这么多,请问大家如果我们的需求是:判断出一个输入有问题后面就不判断了(当然也就不显示了),
   // 怎么办呢?
   // 对了
    if (value.trim().length==0){
                  //...
                  //...
                  //flag=false;  //   flag=false不要去,它的功能是最后如果有问题,不提交数据!
                  return false
            }


//最后,大家尝试着用jquery的绑定来完成这个功能!

      $(".Form :submit").click(function(){});

</script>
```
