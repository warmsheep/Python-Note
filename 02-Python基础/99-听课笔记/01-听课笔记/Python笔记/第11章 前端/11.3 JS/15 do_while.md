## do_while语句
### 基本用法

和while一样，三部曲
* 1.初始化循环变量  
* 2.判断循环条件  
* 3.更新循环变量

```javascript
var 循环变量=值;
do{
  ...
  更新循环变量
  }while(条件)
```

### do_while V.S while
* do_while不管有没有满足while中的条件，do里面的代码都会走一次。
* while是只有循环条件满足才会执行代码。

### do_while举例

```javascript
var i = 3;
do{
  console.log(i)
  i++;

}while (condition)
```
