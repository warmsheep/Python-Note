## FIXME: Hello
### 题目level
* 6kyu

### 题目描述

* 提供的代码有一个方法hello，它应该只显示那些已经明确设置的属性。 此外，它应该按照它们设定的顺序来说。
* 注意:有3个属性:名称、年龄、性别（'M'或'F'）

* 当多次分配相同的属性时，hello方法只显示一次。 如果发生这种情况，顺序取决于该属性的第一次赋值，但该值来自最后一次赋值。

* 举例
```python
Hello.
Hello. My name is Bob. I am 27. I am male.
Hello. I am 27. I am male. My name is Bob.
Hello. My name is Alice. I am female.
Hello. My name is Batman.
```


### 题目思路
* 1.先属性的名称按照属性赋值的顺序依次添加到一个列表中。
* 2.将属性名称-对应的句子按照k-v的模式保存在字典中
* 3.根据列表的顺序从字典中取值，并拼接起来。

### 题目代码
* 我的代码

```python
class Dinglemouse(object):

    def __init__(self):
        self.name = None
        self.sex = None
        self.age = None
        self.list=["hello"]

    def setAge(self, age):
        self.age = age
        if "age" not in self.list:
            self.list.append("age")

        return self

    def setSex(self, sex):
        self.sex = sex
        if "sex" not in self.list:
            self.list.append("sex")
        return self

    def setName(self, name):
        self.name = name
        if "name" not in self.list:
            self.list.append("name")
        return self

    def hello(self):

        dict={
            "hello":"Hello.",
            "name":"My name is {}.".format(self.name),
            "age":"I am {}.".format(self.age),
            "sex":"I am {}.".format("male" if self.sex == "M" else "female")
        }
        return " ".join(dict[x] for x in self.list)
```

* 优秀代码

```python
class Dinglemouse(object):

    def __init__(self):
        self.dct = {}

    def setAge(self, age):
        self.dct['age'] = f'I am {age}.'
        return self

    def setSex(self, sex):
        self.dct['sex'] = f'I am {"male" if sex=="M" else "female"}.'
        return self

    def setName(self, name):
        self.dct['name'] = f'My name is {name}.'
        return self

    def hello(self):
        return ' '.join(['Hello.'] + list(self.dct.values()))
```
### 题目反思
##### 我的代码反思
* 1.通过列表来存储属性赋值的顺序，并不是一个好的办法，这会浪费内存空间。

##### 优秀代码总结
**思路**
* 1.将属性赋值的时候，直接将句子保存在字典里，key:属性名称，value:句子
* 2.针对字典的所有values值通过' '拼接起来，并在开头添加一个'Hello. '

**新学知识点**
* 1.python3.6中的新特性，f表示format的意思:
```python
self.dct['age'] = f'I am {age}.'
#等价于
self.dct['age'] = 'I am {age}.'format(age=age)
```

* 2.字典虽然是无序的，但是如果一开始为空字典，往里面新加key-value，k的显示顺序是k第一次被添加进去的顺序，即使后面对之前的k重新赋值，k的位置依然不变，所以我的列表排序根本就是没有必要的，直接用一个字典就可以解决所有的问题。

* 举个例子来证明知识点2
```python
dic={}
dic["b"]=21
dic["a"]=11
dic["c"]=10
print(dic)
#输出
{'b': 21, 'a': 11, 'c': 10}
```
```python
dic={}
dic["b"]=21
dic["a"]=11
dic["c"]=10
dic["a"]=100
dic["d"]=101
print(dic)
#输出
{'b': 21, 'a': 100, 'c': 10, 'd': 101}
```python
