## Fix string case
### 题目level
* 7kyu

### 题目描述
在这个Kata中，您将得到一个可能混合有大写和小写字母的字符串，您的任务是将该字符串转换为仅使用小写字母还是仅使用大写字母：

尽可能少地做出改变。
如果字符串包含大小写字母相等的数字，请将该字符串转换为小写字母。
例如：
```python
solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
solve("coDE") = "code". Upper == lowercase. Change all to lowercase.
```

### 题目思路
* 1 对字符串中的每个字符进行判断是大写还是小写
* 2 大写则大写计数+1，小写则小写计数+1
* 3 比较两个计数的大小，并将s进行大小写转换

### 题目代码
* 我的代码
```python
def solve(s):
    upper_count = 0
    lower_count = 0
    for i in s:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_count += 1
    if upper_count > lower_count:
        return s.upper()
    else:
        return s.lower()
```

* 优秀代码
```python
def solve(s):
    upper = sum(l.isupper() for l in s)
    lower = sum(l.islower() for l in s)
    return [s.lower(), s.upper()][upper > lower]
```
### 题目反思
##### 我的代码反思
* 我的代码比较繁琐，不太推荐

##### 优秀代码总结
* 1 直接将每个大写小写计数，节约代码行
* 2 将大写和小写放入列表中，索引值为布尔条件，这种方法第一次见，挺厉害的。
