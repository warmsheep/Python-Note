## Product of consecutive Fib numbers
### 题目level
* 5kyu

### 题目描述
* F（m）是最小的一个，例如F（m）* F（m + 1）> prod。
* 例子
```python
productFib（714）#应该返回[21，34，true]
#由于F（8）= 21，F（9）= 34和714 = 21 * 34
productFib（800)#应该返回[34，55，false]，
#F（8）= 21，F（9）= 34，F（10）= 55和21 * 34 <800 <34 * 55
```
* 注意：这里没有用，但我们可以告诉如何选择数字n到哪去：我们可以使用“黄金比例”phi，它是（1 + sqrt（5））/ 2，知道F（n）是渐近的 到：phi ^ n / sqrt（5）。 这给n提供了一个可能的上限。


### 题目思路
* 1.先创造fib函数，定义fib，传入参数n，返回离n最近的b，以及b前面的a组成的列表
```
运用一个定理:a*b=c**2,a != b，那么a,b中一定有一个数大于c，一个数小于c
```
* 2.对主函数的参数prod进行向下取开方数，将这个数传入fib中，得到列表m
* 3.对m中的元素相乘，进行判断:
  * 3.1 如果乘积==prod，则m中追加True
  * 3.2 如果乘积 > prod，则m中追加False
  * 3.3 如果乘积 < prod，则m的b应该再往后取一位数字，解决办法:先追加sum(m)，再追加一个False，然后取值应该从第2位元素到最后一位元素。



### 题目代码
* 我的代码
```python
import math
def fib(n):
    a, b = 0, 1
    while b <= n:
        a, b = b, a + b
    return [a,b]
def productFib(prod):
    s=math.floor(math.sqrt(prod))
    m=fib(s)
    if m[0]*m[1]==prod:
        m.append(True)
        return m

    elif m[0]*m[1] < prod:
        m.append(sum(m))
        m.append(False)
        return m[1:]
    else:
        m.append(False)
        return m
```

* 优秀代码

```python
def productFib(prod):
    a, b = 0, 1
    while prod > a * b:
        a, b = b, a + b
    return [a, b, prod == a * b]
```

### 题目反思
##### 我的代码反思
* 1.反思结果:我的代码对条件写的太多了，导致了代码数量很长很长
* 2.其实返回一个列表我也不是很满意，但是为了后面的追加，我才用的，继续努力吧，第一个5kyu的题目。

##### 优秀代码总结
**思路**
* 1.对fib函数进行一个条件循环，循环条件为:prod>a\*b，这样避免了条件讨论a*b和prod的比较，因为当a\*b=prod时候，循环结束了。
* 2.然后返回一个列表，列表中有一个bool值，条件为prod==a*b
