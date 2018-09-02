## for语句
### 基本用法

##### for分三步走
* 1.初始化循环变量
* 2.判断循环语句
* 3.更新循环语句

```javascript
if(初始化循环变量;判断循环语句;更新循环语句){
  ...
}
```

### for举例
##### 1.1-100之间所有的偶数
```javascript
for(var i=1;i<=100;i++){
  	if(i%2==0){
  		console.log(i)
  	}
  }
```

##### 2.计算1-100之间所有的和
```javascript
var sum=0;
for(var i=1;i<=100;i++){
	sum+=j
}
console.log(sum)
```

##### 3.打印3行6列*号
```javascript
for(var i=1;i<=3;i++){
	for(var j=0;j<=6;j++){
		document.write("*")
	}
	document.write("<br/>")
}
```

### 作业
##### 1.输出6行直角三角形
```javascript
for(var i=1;i<=6;i++){
  for(j=1;j<=i;j++){
    document.write("*")
  }
  document.write("<br/>")
}
```

##### 2.输出6行等边三角形
```javascript
for(var i=1;i<=6;i++){
  for(j=i;j<=6;j++){
    document.write("&nbsp;")
  }

  for(k=1;k<=(2*i-1);k++){
    document.write("*")
  }
  document.write("<br>")
}
```
