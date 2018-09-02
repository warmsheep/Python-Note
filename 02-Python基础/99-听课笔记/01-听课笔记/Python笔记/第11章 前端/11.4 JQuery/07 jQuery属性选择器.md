## jQuery属性选择器

### $(标签名[属性名])
查找所有含id属性的该标签名的元素
```javascript
$('li[id]').css('color','red')
```
### $(标签名[attr=value])
匹配给定的属性时某个特定值的元素
```javascript
$('li[class=what]').css('color','green')
```
### $(标签名[attr!=value])
匹配不含指定的属性时某个特定值的元素，或者属性不等于特定值的元素

```javascript
$('li[class=!what]').css('color','grey')
```
### $(标签名[attr^=value])
匹配给定的属性是以某些之开始的元素
```javascript
$('input[name^=username]').css('background','pink')
```
