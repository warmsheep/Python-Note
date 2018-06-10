## jQuery对象和DOM对象转换
### DOM对象转换为jQuery对象

```javascript
var box = document.getElementById("box");
console.log($(box));
```

### jQuery对象转换为DOM对象
##### 方法一
```javascript
$('button')[0]
```

##### 方法二
```javascript
$('button').get(0)
```
