# re模块

正则表达式就是字符串的匹配规则，在多数编程语言里都有相应的支持，python里对应的模块是re

## 常用的表达式规则

| 符号 | 规则 |
|:-- |:-- |
| . | 默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行 |
| ^ | 匹配字符开头，若指定flags MULTILINE,这种也可以匹配上(r"^a","\nabc\neee",flags=re.MULTILINE) |
| $ | 匹配字符结尾， 若指定flags MULTILINE ,re.search('foo.$','foo1\nfoo2\n',re.MULTILINE).group() 会匹配到foo1 |
| * | 匹配*号前的字符0次或多次， re.search('a*','aaaabac')  结果'aaaa' |
| + | 匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']|
| ? | 匹配前一个字符1次或0次 | ,re.search('b?','alex').group() 匹配b 0次
| {m} | 匹配前一个字符m次 ,re.search('b{3}','alexbbbs').group()  匹配到'bbb' |
| {n,m} | 匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果'abb', 'ab', 'abb'] |
| | | 匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果'ABC' |
| (...) | 分组匹配， re.search("(abc){2}a(123|45)", "abcabca456c").group() 结果为'abcabca45' |
| \A | 只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的，相当于re.match('abc',"alexabc") 或^ |
| \Z | 匹配字符结尾，同$ |
| \d | 匹配数字0-9 |
| \D | 匹配非数字 |
| \w | 匹配[A-Za-z0-9] |
| \W | 匹配非[A-Za-z0-9] |
| s | 匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t'|
| (?P<name>...) | 分组匹配 re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").groupdict("city") 结果{'province': '3714', 'city': '81', 'birthday': '1993'}|


## re的匹配语法有以下几种
* **re.match 从头开始匹配**
* **re.search 匹配包含**
* **re.findall 把所有匹配到的字符放到以列表中的元素返回**
* **re.split 以匹配到的字符当做列表分隔符**
* **re.sub 匹配字符并替换**
* **re.fullmatch 全部匹配**

**re.compile(pattern, flags=0)**

将正则表达式模式编译为正则表达式对象，该对象可用于使用match（），search（）和其他方法进行匹配，如下所述。

The sequence

```python
prog = re.compile(pattern)
result = prog.match(string)
```

is equivalent to

```python
result = re.match(pattern, string)
```

但如果在单个程序中多次使用表达式，则使用re.compile（）并保存生成的正则表达式对象以便重用将会更有效。

**re.match(pattern, string, flags=0)**

从起始位置开始根据模型去字符串中匹配指定内容，匹配单个

* pattern 正则表达式
* string 要匹配的字符串
* flags 标志位，用于控制正则表达式的匹配方式

```python
import re
obj = re.match('\d+', '123uuasf')
if obj:
    print obj.group()
```

**Flags标志符**

* re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同）
* M(MULTILINE): 多行模式，改变'^'和'$'的行为
* S(DOTALL): 改变'.'的行为,make the '.' special character match any character at all, including a newline; without this flag, '.' will match anything except a newline.
* X(re.VERBOSE) 可以给你的表达式写注释，使其更可读，下面这2个意思一样


```
a = re.compile(r"""\d + # the integral part
                \. # the decimal point
                \d * # some fractional digits""",
                re.X)

b = re.compile(r"\d+\.\d*")

```

**re.search(pattern, string, flags=0)**

根据模型去字符串中匹配指定内容，匹配单个

```python
import re
obj = re.search('\d+', 'u123uu888asf')
if obj:
    print obj.group()
```

**re.findall(pattern, string, flags=0)**

match and search均用于匹配单值，即：只能匹配字符串中的一个，如果想要匹配到字符串中所有符合条件的元素，则需要使用 findall。

```python
import re
obj = re.findall('\d+', 'fa123uu888asf')
print obj
```

**re.sub(pattern, repl, string, count=0, flags=0)**

用于替换匹配的字符串

```python
re.sub('[a-z]+','sb','武配齐是abc123',)

re.sub('\d+','|', 'alex22wupeiqi33oldboy55',count=2)
'alex|wupeiqi|oldboy55'
```

相比于str.replace功能更加强大


**re.split(pattern, string, maxsplit=0, flags=0)**

整个字符串匹配成功就返回re object, 否则返回None

```python
re.fullmatch('\w+@\w+\.(com|cn|edu)',"alex@oldboyedu.cn")
```
