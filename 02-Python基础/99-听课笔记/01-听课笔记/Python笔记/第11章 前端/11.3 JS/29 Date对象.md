## Date对象
### 创建日期
* new Date()
```javascript
var myDate = new Date();
```

### 获取一个月中的某一天
* myDate.getDate()
```javascript
```
### 获取当天的日期和时间
* Date()
```javascript
console.log(Date())
```

### 获取一年中的第几个月
* 1月-12月(0-11)
```javascript
console.log(myDate.getMonth()+1)
```
### 获取周几
* 周日-周六(0-6)
```javascript
console.log(myDate.getDay())
```
### 将Date对象转换为字符串
* myDate.toString()
```javascript
var d=new Date()
document.write(d.toString())
```
