## while

### 基本语法
* 1.初始化循环变量
* 2.判断循环条件
* 3.更新循环变量

```javascript
var 循环变量=值;
while(condition){
  ...
  更新循环变量
}
```

### 举个例子

```javascript
var i = 1;

while(i<=9){
  console.log(i)
  i+=1;
}
```

### 练习
将1-100之间的所有是3的倍数输出

```javascript
var j=1;
while(j<=100){
  if(j%3==0){
    console.log(j)
  }
  j++;
  }
```
