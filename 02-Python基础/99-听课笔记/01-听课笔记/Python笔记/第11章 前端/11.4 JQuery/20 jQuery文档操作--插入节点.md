## jQuery文档操作--插入节点
### 父元素.append(子元素)
追加某元素，父元素中添加新的元素
```javascript
var oli = document.createElement("li");
oli.innerHTML='哈哈哈'
//jQuery中的dom操作
//1.append(content)追加 往父元素中添加新的元素
//content:string | element | jquery元素
//追加元素
$('ul').append("<li>1234</li>")
$("ul").append(oli)
//如果直接的内容是当前页面中的某些元素，那么这些元素将从原位置上消失，简言之就是一个移动操作
$("ul").append($("#app"))
```

### 子元素.appendTo(父元素)
追加到某元素，子元素添加到父元素
