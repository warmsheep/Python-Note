## Correct the mistakes of the character recognition software
### 题目level
* 8kyu

### 题目描述
字符识别软件广泛用于数字化打印文本。 因此文本可以被编辑，搜索并存储在计算机上。

当文件（特别是用打字机写的很旧的文件）时，数字化的字符识别软件经常会出错。

你的任务是正确的数字化文本中的错误。 你只需要处理以下错误：

* S is misinterpreted as 5
* O is misinterpreted as 0
* I is misinterpreted as 1


### 题目思路
* 1.利用maketrans建立映射表
* 2.然后用translate进行替换

### 题目代码
* 我的代码

```python
def correct(string):
    intab = "501"
    outtab = "SOI"
    trantab = str.maketrans(intab,outtab)
    return string.translate(trantab)
```

* 优秀代码
```python
def correct(string):
    return string.translate(str.maketrans("501", "SOI"))
```
```python
def correct(string):
    return string.replace('1','I').replace('0','O').replace('5','S')
```

### 题目反思
##### 我的代码反思
* 1.看见这道题第一反应就是用maketrans+translate，但是我的方法是一步一步来的，不是很简洁。
* 2.maketrans+translate方法介绍

**maketrans() 方法语法：**

Python3中：
```python
str.maketrans(intab,outtab[,delchars])
```

Python2中：

```python
import string
string.maketrans(intab,outtab)
```

**参数**

* intab -- 需要转换的字符组成的字符串。
* outtab -- 转换的目标字符组成的字符串。
* delchars -- 可选参数，表示要删除的字符组成的字符串。

**返回值**

返回一个字符映射转换表供 translate() 方法调用。

##### 优秀代码总结
* 方法一比较简洁
* 方法二提供了replace方法来做，本题替代量小可以这么做，但是如果替换的字母很多，不建议这样。
