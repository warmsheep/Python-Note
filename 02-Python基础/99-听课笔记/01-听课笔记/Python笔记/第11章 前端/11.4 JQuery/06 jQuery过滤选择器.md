## jQuery过滤选择器

### :first
获取第一个元素
```javascript
$('li:first').text("hello")
```

### :last
获取最后一个元素
```javascript
$('li:last').html('world')
```

### :odd
匹配所有索引值为奇数的元素，从0开始计数
```javascript
$('li:odd').css('color','green')
```

### :even
匹配所有索引值为偶数的元素，从0开始计数
```javascript
$('li:even').css('color','green')
```

### :eq(index)
获取给定索引值的元素，从0开始计数
```javascript
$('li:eq(1)').css('font-size','40px')
```

### :gt(index)
匹配所有大于给定索引值的元素
```javascript
$('li:gt(2)').css('background-color','green')
```

### :lt(index)
匹配所有小于给定索引值的元素
```javascript
$('li:lt(2)').css('background-color','grey')
```
