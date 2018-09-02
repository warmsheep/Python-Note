## jQuery筛选选择器
### $(属性名).eq(n)
获取第n个元素，数值从0开始

```javascript
$('span').eq(0).css('font-size','30px')
```

### $(属性名).first()
点语法:get方法和set方法
对象才有方法，jQuery方法中get后也是对象
获取第一个元素

```javascript
$('span').first().css('background','red')
```
### $(属性名).last()
获取最后一个元素

```javascript
$('span').last().css('background','red')
```
### $(属性名).parent()
选择父亲元素

```javascript
$('span').partent().css({'width':300px,'height':200px})
```

### $(属性名).siblings()
选择所有的兄弟元素
```javascript
$('.list').siblings('li').css('color','red')
```

### $(属性名).find(属性名)
查找后代元素
```javascript
$('div').find('button').css('background','yellow')
```
