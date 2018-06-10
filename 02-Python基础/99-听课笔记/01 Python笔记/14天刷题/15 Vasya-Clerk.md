## Vasya - Clerk
### 题目level
* 6kyu

### 题目描述
* 新的“复仇者”电影刚刚发布！ 电影票房有很多人站在一条巨大的线上。 他们每个人都有一张100美元，50美元或25美元的账单。 “复仇者”票价25美元。

* Vasya目前是一名职员。 他想把票卖给这条线上的每一个人。

* Vasya可以向每个人出售一张门票，如果他最初没有钱，可以给予改变，并严格按照人们遵循的顺序销售门票？

* 返回YES，如果Vasya可以向每个人出售一张票，并在那个时刻用他手头的账单进行更改。 否则返回NO。

```python
tickets([25, 25, 50]) # => YES
tickets([25, 100])
         # => NO. Vasya will not have enough money to give change to 100 dollars
```

### 题目思路
* 1.新建一个列表In，遍历people里的每个元素，再进行判断
  * 1.1 如果值是25，则添加到In
  * 1.2 如果是50，则In移除一个25，并添加一个50
  * 1.3 如果值是100，如果In中没有25，直接返回NO，且In中有25，则进行以下分类讨论:
    * 1.3.1 先判断In里面有没有50，如果有的话，就移除一个50和25
    * 1.3.2 如果In里面没有50，则移除3个25
  * 1.4 异常处理，针对出现的可能In中移除元素出现的ValueError，用try...except处理异常。

### 题目代码
* 我的代码
```python
def tickets(people):
    In=[]
    try:
        for i in people:
            if i == 25:
                In.append(i)
            elif i == 50:
                In.remove(25)
                In.append(50)
            elif i == 100:
                if  25 in In:
                    if 50 in In:
                        In.remove(50)
                        In.remove(25)
                    else:
                        In.remove(25)
                        In.remove(25)
                        In.remove(25)
                else:
                    return "NO"
        return "YES"
    except ValueError:
        return "NO"
```
* 优秀代码
```python
def tickets(a):
    n25 = n50 = n100 = 0
    for e in a:
        if   e==25            : n25+=1
        elif e==50            : n25-=1; n50+=1
        elif e==100 and n50>0 : n25-=1; n50-=1
        elif e==100 and n50==0: n25-=3
        if n25<0 or n50<0:
            return 'NO'
    return 'YES'
```
### 题目反思
##### 我的代码反思
* 1.我的代码比较冗余，但是思想而言，和优秀代码是一样的，表达方式不太好。
* 2.优秀代码中用了字符串来表示，而我用了列表，浪费内存空间
* 3.用字符串计数比用列表中移除更方便，我的代码remove用了好多次，但是用字符串计数直接用运算符即可。

##### 优秀代码总结
* 1.用n25,n50,n100进行计数，初始化值都为0
* 2.对a中的元素进行遍历:
  * 2.1 如果a=25，则n25+=1
  * 2.2 如果a=50,n25-=1，n50+=1
  * 2.3 如果a=100且n50的值>0，则n50-=1，n25-=1
  * 2.4 如果a=100且n50的值=0，则n25的值-=3
* 3.针对计算后的结果来判断，如果n25或n50的值小于0，则返回NO，反之返回YES。
