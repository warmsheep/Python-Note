## Number对象
### num.toString()
将number类型转换成字符串类型

```javascript
var num = 132.32222;
var numStr = num.toString()
console.log(typeof numStr)
//str
```

### num.toFixed(n)
对数字四舍五入，保留n位小数
```javascript
var newNum = num.toFixed(1)//132.3
```
