## Exclamation marks series #6: Remove n exclamation marks in the sentence from left to

### 题目level
* 8kyu

### 题目描述

描述：
从左到右删除句子中的n个感叹号。 n是正整数。
```python
remove("Hi!",1) === "Hi"
remove("Hi!",100) === "Hi"
remove("Hi!!!",1) === "Hi!!"
remove("Hi!!!",100) === "Hi"
remove("!Hi",1) === "Hi"
remove("!Hi!",1) === "Hi!"
remove("!Hi!",100) === "Hi"
remove("!!!Hi !!hi!!! !hi",1) === "!!Hi !!hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",3) === "Hi !!hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",5) === "Hi hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",100) === "Hi hi hi"
```

### 题目思路
* 利用replace方法来进行替换

### 题目代码
* 我的代码
```python
def remove(s, n):
    return s.replace("!","",n)
```
* 优秀代码
```python
remove=lambda s,n:s.replace('!','',n)
```

### 题目反思
##### 我的代码反思
* replace知识点总结
replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。

replace()方法语法：
```python
str.replace(old, new[, max])
```
##### 优秀代码总结
用匿名函数完成该题。
