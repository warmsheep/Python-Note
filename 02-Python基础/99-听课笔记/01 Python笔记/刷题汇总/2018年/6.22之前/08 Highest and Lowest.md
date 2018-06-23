## 查找最大最小值
### 题目level
* 7kyu

### 题目描述
* 在这个小小的任务中，您会得到一串空格分隔的数字，并且必须返回最高和最低数字。
* 举例:
```python
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
```

### 题目思路
* 1.因为负数和正数在一起的排序不会，所以我采用了找到find the  parity outlier 中优秀代码的方法(学以致用的感觉很不错)
* 2.将字符串分割，正数放在pos列表，负数放在neg列表
* 3.对列表进行排序取值。
* 4.考虑pos或neg列表存在空列表的情况。


### 题目代码
* 我的代码
```python
def high_and_low(numbers):
    l=numbers.split(" ")
    neg=[int(x) for x in l if int(x)<0]
    pos=[int(x) for x in l if int(x)>=0]
    #考虑存在空列表的情况
    if not neg:
        return "%d %d"%(sorted(pos)[-1],sorted(pos)[0])
    elif not pos:
        return "%d %d"%(sorted(neg)[-1],sorted(neg)[0])
    return "%d %d"%(sorted(pos)[-1], sorted(neg)[0])
```

* 优秀代码
```python
def high_and_low(numbers):
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
```

### 题目反思
##### 我的代码
* 1.总体来说我的代码并不节省内存资源(创建了两个列表)，而且还存在情况讨论，还是存在超级大的改进空间的。

##### 优秀代码
* 1.针对列表直接使用max，min方法，感觉更高效、便捷，只使用了一个列表，节省字符空间，也不用讨论那么多的情况，很厉害的解法。
