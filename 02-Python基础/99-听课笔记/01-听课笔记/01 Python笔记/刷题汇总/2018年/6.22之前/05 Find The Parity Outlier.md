## 找到奇偶异常值
### 题目level
* 6kyu

### 题目描述
* 给你一个包含整数的数组（它的长度至少为3，但可能非常大）。 该数组要么完全由奇数整数组成，要么完全由偶数整数组成，除了一个整数N.编写一个将数组作为参数并返回此“异常值”的方法N.

* 举例

```python
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
```

### 解题思路
* 1.integers列表中只有奇偶数，新建空列表l，对integers列表中每遇到一个奇数往l中添加"A"，偶数添加"B"
* 2.对l中的AB计数，计数为1的那个值为异常值，这个值在l中的index就是异常值在integers的的位置。

### 解题代码
* 我的代码

```python
def find_outlier(integers):
    l=[]
    for i in integers:
        if i%2==0:
            l.append("A")
        else:
            l.append("B")
    if l.count("A")==1:
        return integers[l.index("A")]
    else:
        return integers[l.index("B")]
```

* 优秀代码

```python
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]
```

### 题目反思
##### 我的代码总结
* 1.主要是根据题目中的异常值个数为1，而且都奇数或者偶数，运用运算的区别来将异常值找出。

##### 优秀代码总结
* 1.新建了两个空列表奇数列表odds和偶数列表evens，针对int中每个值的奇偶性分别添加。
* 2.因为异常值数目只有1个，所以odds和evens的列表的长度不一样，选长度为题目中的异常值。
