## 求和:二维数组的积-二维数组最小公倍数

### 题目level
* 7kyu

### 题目描述

* 在这个kata中，您需要创建一个函数，该函数采用非负整数对的二维数组/列表，并返回所有“保存”的总和，您可以获得每个数字的LCM与其简单产品的比较。

* For example, if you are given:
```
[[15,18], [4,5], [12,60]]
```
* 每个二维数组的乘积为:
```
[270, 20, 720]
```
* 每个二维数组的最小公倍数为:
```
[90, 20, 60]
```
* 最终结果为:
```
(270-90)+(20-20)+(720-60)==840
```
### 解题思路
* 1.这道题的题意很清楚:
```
SUM(二维数组的积-二维数组的最小公倍数)
```
* 2.第一步先考虑求二维数组的积
* 3.求二维数组的最小公倍数(本题难点)


### 解题代码
* 我的代码
```python
def gcd(m,n):
    if not n:
        return m
    else:
        return gcd(n, m%n)

def LCM(m, n):
    if m*n == 0:
        return 0
    return int(m*n/gcd(m, n))

def sum_differences_between_products_and_LCMs(pairs):
    result=0
    for i in pairs:
        result+=(i[0]*i[1]-LCM(i[0], i[1]))
    return result
```

* fork解答

```python
def gcd(a,b):
    min_val, max_val = min(a,b), max(a,b)
    while min_val:
        min_val, max_val = max_val % min_val, min_val
    return max_val

def lcm(a,b):
    return (a*b) / gcd(a,b)

def sum_differences_between_products_and_LCMs(pairs):
    return sum(0 if not a*b else a*b - lcm(a,b) for a,b in pairs)
```


### 题目反思
* 1.解题难点在于如何求最小公倍数
##### 如何求最小公倍数？
* 公式
```
最小公倍数 = 乘积 / 最大公约数
```
这个问题转化为如何求最大公约数。

##### 如何求最大公约数(自己总结)

*网上经验帖总结*

* 1. 如果两者中有一个数字为0，则另一个数字为最大公约数。
* 2. 如果两个数字都不为0，则两者相除取余数，并调换参数位置，余数再来和另外一个数字求公倍数，最终获得最大公约数。(这里用到递归的方法，可以试着写几个例子去验证一下)

*网上经验贴代码如下*

```python
def gcd(m,n):

    if not n:
        return m
    else:
        return gcd(n, m%n)
```

*fork解法*

* 1.先找到两个数的最大值和最小值
* 2.最小值不为0的情况下:
  * 最大值%最小值 取余数，将余数重新赋值给最小值，之前的最小值成为最大值
```
(这里是为啥？因为a/b的余数，是永远不可能大于等于b的，所以最大值除最小值的余数肯定小于最小值，所以余数应该成为新的最小值)
```
* 3.当余数为0的时候，说明被除的整数为两个数字的最大公约数。

```python
def gcd(a,b):
    min_val, max_val = min(a,b), max(a,b)
    while min_val:
        min_val, max_val = max_val % min_val, min_val
    return max_val
```
