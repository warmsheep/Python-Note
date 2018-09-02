## The wheat/rice and chessboard problem
### 题目level
* 7kyu

### 题目描述
* 我假定你们大多数人都熟悉大米的古老传说（但是我看到维基百科建议小麦出于某种原因）的问题，但是对你来说很快就会有一个回顾：一个年轻人在第一个问题时要求赔偿1粒米 平方米，第二个2粒，第三个4个，第四个8个等，总是翻倍。

* 你的任务是非常简单的（但不一定容易）：给定一定数量的谷物，你需要返回到应该计算的棋盘格的平方，以获得至少同样多的棋盘。

* 像往常一样，一些例子可能比我的成千上万的话更好：

squares_needed(0) == 0
squares_needed(1) == 1
squares_needed(2) == 2
squares_needed(3) == 2
squares_needed(4) == 3

* 输入始终是有效/合理的：即：非负数; 额外的cookie不使用循环来逐一计算（至少不是直接），而是尝试更聪明的方法[提示：一些特殊的操作符]; 转换数字的技巧也可能奏效：打动我！


### 题目思路
* 1.将grains用log2运算
* 2.排除grains为0的情况

### 题目代码
* 我的代码
```python
import math
def squares_needed(grains):
    return int(math.log(grains,2))+1 if grains != 0 else 0
```

* 优秀代码
```python
def squares_needed(grains):
    return (len(bin(grains)) - 2) * (grains > 0)
```

### 题目反思
##### 我的代码反思
* 1.用到了对数函数，如果不指定base，默认base为e
```python
math.log(x[,base])
```
* 2.int取整默认为向下取整，和floor取整的道理一样。

##### 优秀代码总结
* 1.由于是2的幂次方，所以使用了bin，将数字转化为2进制，然后取二进制的位数
* 2.默认二进制的样式为0bxxxxx，所以在取得的二进制的长度的基础上需要减掉2，得到最终的长度。
* 3.考虑grains为0的情况，当grains为0时，长度为1，解决办法:用一个布尔值来相乘，布尔值的条件为(grains>0)

##### 补充知识点
* 取整:int()
int取整其实就是向下取整和math.floor()取整的效果一样

```python
int(num)
```
```python
print(int(3.2),int(3.5))
3 3
```
* 向上取整:math.ceil()
```python
``python
import math
math.ceil(num)
```
```python
import math
print(math.ceil(3.2),math.ceil(3.5))
4 4
```
* 向下取整:math.floor()

```python
import math
math.floor(num)
```
```python
import math
print(math.floor(3.2),math.floor(3.5))
3 3
```

* 四舍五入取整:round()

```python
round(num)
```
```python
import math
print(round(3.2),round(3.5))
3 4
```
