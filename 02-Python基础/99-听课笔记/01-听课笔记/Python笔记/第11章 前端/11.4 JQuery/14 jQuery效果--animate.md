## jQuery效果--animate
### animate
概念:用于创建自定义动画的函数
语法:animate(params,[speed],[fn])
参数:
params:一组包含作为动画属性和终值的样式值及其值的集合
speed:三种预定速度之一的字符串('slow','normal','fast')或表示动画时长的毫秒数值(如:1000)
fn:在动画完成时执行的函数，每个元素执行一次。


### stop
概念:停止所有在指定元素上正在运行的动画
语法:stop([clearQueue],[jumpToEnd])
参数:
clearQueue:如果设置为true，则清空列队。可以立即结束动画
gotoEnd:让当前正在执行的动画立即完成，并且重设show和hide的原始样式，调用回调函数等。

### delay
概念:用来做延迟的操作
语法:delay(1000)，一秒之后做后面的操作
