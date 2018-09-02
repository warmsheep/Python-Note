## Letterbox Paint-Squad
### 题目level
* 7kyu

### 题目描述
* 故事

你和一群朋友在学校的假期中赚取了一些额外的钱，只需少量费用就可以在人们的信箱上重新绘制数字。

既然你们中有10个人每个人都只专心画一个数字！ 例如，有人只画1，其他人只画2，等等......

但在一天结束时，你意识到并不是每个人都做了相同的工作量。

为了避免任何战斗，你需要公平分配资金。 这就是卡塔进来的地方。

* 卡塔任务
给定开始和结束的信箱号码，写一个方法返回绘制的所有10位数字的频率。

* 举例
开始= 125，结束= 132

信箱是
```
125 = 1, 2, 5
126 = 1, 2, 6
127 = 1, 2, 7
128 = 1, 2, 8
129 = 1, 2, 9
130 = 1, 3, 0
131 = 1, 3, 1
132 = 1, 3, 2
```

数字频率是1 x 0，9 x 1，6 x 2等...
所以该方法会返回
```
[1,9,6,3,0,1,1,1,1,1]
```

### 解题思路
* 1.先将0-9作为键，0作为值，将Counter初始化(注意数字应为字符形式)
* 2.迭代区间内的值，然后将值转为字符串再对Counter进行更新
* 3.对Counter进行排序，排序依据为key，并将排序后的字典values值提取，格式为列表形式(排序后的Counter会变成元组形式，需要先将它转换为字典形式，再进行去value值，再对value值转化成列表)


### 解题代码
* 我的代码
```python
from collections import Counter
import operator
def paint_letterboxes(start, finish):
    c = Counter()
    for i in range(10):
        c[str(i)]=0
    for i in range(start,finish+1):
        c.update(str(i))
    result=list(dict(sorted(c.items(),key=operator.itemgetter(0))).values())
    return result
```

* 优秀代码

```python
from collections import Counter

def paint_letterboxes(s, f):
    a = Counter("".join(map(str, range(s, f+1))))
    return [a[x] for x in "0123456789"]
```

* 我的代码优化

```python
def paint_letterboxes(start, finish):
    c = Counter()
    for i in range(start,finish+1):
        c.update(str(i))
    return [c[x] for x in "0123456789"]
```

### 题目反思
##### 我的代码反思
* 1.针对我的代码，可以说是后面的都是拼起来的，排序后是元组-->转化成字典--->提取values值--->将值转化为列表
* 2.我的代码很繁琐，但是把今天学的两个知识点都用到了，一个是operator模块，一个是Counter模块，还是很开心的。

##### 优秀代码总结
* 1.用到map函数将迭代区间内的值转换为字符串
  * map的用法(其实我是知道这个用法的，但是用之极少，以后多多练习，试着多用才能提升)
  ```python
  map(function, iterable, ...)
  ```
* 2.将迭代区间内的所有字符串拼接起来，然后用Counter来进行计算键值。

  * join在这里用我感觉真的是绝了，虽然做题的时候我也想过将所有的数字拼接起来，但是说实话没多想，因为自己一时想不到，长知识了。

* 3.最后一个用法，成功的使用了counter中一个属性:对Counter中查找键对应的值，如果该键不存在，Counter会返回0。

* 4.最后一个写法也是很不错的，虽然总是学不会，多多看看总是好的。
```python
return [a[x] for x in "0123456789"]
```

* 5.分析了优秀代码的思路和写法之后，将自己的代码优化了，看起来舒服多了，哈哈哈。
