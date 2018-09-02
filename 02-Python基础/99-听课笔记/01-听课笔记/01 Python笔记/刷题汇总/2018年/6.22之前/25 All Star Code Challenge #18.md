## All Star Code Challenge \#18

### 题目level
* 8kyu

### 题目描述

创建一个名为that的函数接受2个字符串参数，并返回在第一个参数中找到的第二个参数的出现次数的整数。

如果没有发现，应返回0的计数。


### 题目思路
* 1.由于字符串是可迭代的，所以直接利用count计数

### 题目代码
* 我的代码

```python
def str_count(strng, letter):
    return strng.count(letter)
```

* 优秀代码
```python
str_count = lambda strng, letter: strng.count(letter)
```

### 题目反思
##### 我的代码反思
* 1.常用方法不必多说

##### 优秀代码总结

* 1.为什么把优秀代码选这个呢，因为第一，本人对lambda函数生疏，第二，lambda函数的用处实在是太大了。

本题中的lambda的用法，
```python
str_count = lambda strng, letter: strng.count(letter)
```
调用方式:
```python
str_count(strng, letter)
```

举例:
```python
add = lambda x, y : x+y
add(1,2)  # 结果为3
```
