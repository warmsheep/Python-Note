## String对象
### str.length
字符串的长度
* 直接为str.length，不是str.length()

```javascript
var str="hello alex"
console.log(str.length)//10
```

### str.toUpperCase()
转化成大写
```javascript
var bigStr=str.toUpperCase()//HELLO ALEX
```

### str.toLowerCase()
转化成小写
```javascript
var smallStr=bigStr.toLowerCase()//hello alex
```

### str.split('',n)
第一个以什么分割，第二个限制分割后的数字的长度,只会取n个元素
```javascript
var newArr = str.split(" ",1)
console.log(newArr)
//['hello']
```

### str.substring(n:m)
提取字符串中index从第n个到第m-1个值,左闭右开，会返回一个新的字符串
```javascript		
var a=str.substring(2,6)
console.log(a)
//llo
```
