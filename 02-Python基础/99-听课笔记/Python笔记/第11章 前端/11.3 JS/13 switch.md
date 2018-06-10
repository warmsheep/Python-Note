## switch
switch开关
* switch一般和case连用。
* case表示一个条件，满足这个条件就会走进来，遇到break跳出。
* default表示默认。

**注意**
在case后面必须要写上break.

### 基本语法

```javascript
switch(查找的内容){
  case 条件1:
  ...
  break;

  case 条件2:
  ...
  break;

  ...

  default:
  ...

}
```

### switch举例

```javascript
//switch开关
var gameScore="better"
//与case连用
switch(gameScore){
  //case表示一个条件，满足这个条件就会走进来，遇到break调出
  case "good":
  console.log("很棒哦")
  //break表示退出
  break;

  case "better":
  console.log("玩的老牛逼了")
  break;

  case "best":
  console.log("超神！")
  break;

  default:
  console.log("下次加油")
}
```
