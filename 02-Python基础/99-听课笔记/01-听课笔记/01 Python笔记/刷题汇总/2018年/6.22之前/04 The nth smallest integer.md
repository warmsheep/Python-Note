## 取第n个最小值
### 题目level
* 6kyu

### 题目描述:

* 给定一个整数列表，返回列表中第n个最小的整数。 计算答案时只应考虑不同的元素。 n总是正数（n> 0）

* 如果第n个小整数不存在，则返回-1（C ++）/ None（Python）/ nil（Ruby）。

### 解题思路:
* 1.整数列表去重
* 2.整数列表排序
* 3.整数列表取第n个值
* 4.处理异常Indexerror，并返回None

### 解题代码:

* 我的代码

```python
def nth_smallest(arr, n):
    try:
        return sorted(list(set(arr)))[n-1]
    except IndexError:
        return None
```

* 最佳代码
```python
def nth_smallest(arr, n):
    s = set(arr)
    return sorted(s)[n-1] if n<=len(s) else None
```

### 题目总结
##### 我的解答总结
* 1.列表如何去重:list-->set
* 2.列表如何排序:sorted
* 3.列表取第n个小的值，序列号为n-1
* 4.出现Indexerror处理机制:try...except解决
* 5.直接返回None而不是"None"

##### 最优解答总结
* 1.一直以为集合是不可以排序的，其实集合也可以用sorted排序，涨知识了。
* 2.如果用最优解答的方式，我的也可以优化一下，变成下面这样:

```python
def nth_smallest(arr, n):
    s=list(set(arr))
    return sorted(s)[n-1] if n<=len(s) else None
```
