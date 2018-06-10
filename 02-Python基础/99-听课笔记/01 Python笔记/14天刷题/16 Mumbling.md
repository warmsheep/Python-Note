## Mumbling
### 题目level
* 7kyu

### 题目描述
* 这一次没有故事，没有理论。 以下示例显示如何编写函数accum：
```python
accum("abcd")    # "A-Bb-Ccc-Dddd"
accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt")    # "C-Ww-Aaa-Tttt"
```

### 题目思路
* 1.对字符串使用enumerate()，取到k,v值
* 2.对每个v*(k+1),然后对整个字符串首字母大写方法capitalize()

### 题目代码
* 我的代码
```python
def accum(s):
    return "-".join([(v*(k+1)).capitalize()  for k,v in enumerate(s)])
```
* 优秀代码
```python
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
```
### 题目反思
##### 我的代码总结
* str.capitalize()也可以换做str.title()

##### 优秀代码总结
* 1.将字符串第一个大写，后面重复的小写，然后拼接起来，和我的方法不一样，学习了。
