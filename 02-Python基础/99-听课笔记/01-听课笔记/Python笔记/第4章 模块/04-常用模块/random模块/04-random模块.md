# random模块

## random.random

random.random()用于生成一个0到1的随机符点数: 0 <= n < 1.0

```python
import random
s=random.random()
print(s)

0.3014504126832446
```

## random.uniform

random.uniform(a, b)，用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限。如果a > b，则生成的随机数n: a <= n <= b。如果 a <b， 则 b <= n <= a

```python
i1=random.uniform(10,20)
i2=random.uniform(20,10)
print(i1,i2)

12.811094498878653 11.576520114846792
```

## random.randint

random.randint(a, b)，用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b

```python
i3=random.randint(10,20)
print(i3)

19
```

## random.randrange

random.randrange([start], stop[, step])，从指定范围内，按指定基数递增的集合中 获取一个随机数。如：random.randrange(10, 100, 2)，结果相当于从[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数。random.randrange(10, 100, 2)在结果上与 random.choice(range(10, 100, 2) 等效

```python
i4=random.randrange(10,100,3)
print(i4)

37
```

## random.choice

random.choice从序列中获取一个随机元素。其函数原型为：random.choice(sequence)。参数sequence表示一个有序类型。这里要说明 一下：sequence在python不是一种特定的类型，而是泛指一系列的类型。list, tuple, 字符串都属于sequence。有关sequence可以查看python手册数据模型这一章。下面是使用choice的一些例子：

```python
print(random.choice("学习Python"))#字符串
t

print(random.choice(["JGood", "is", "a", "handsome", "boy"]))#列表
boy

print(random.choice(("Tuple", "List", "Dict")))#元组
Dict
```

## random.shuffle
random.shuffle(x[, random])，用于将一个列表中的元素打乱。如:

```python
p = ["Python", "is", "powerful", "simple", "and so on..."]
random.shuffle(p)
print(p)

['and so on...', 'powerful', 'simple', 'is', 'Python']
```

## random.sample

random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。**sample函数不会修改原有序列**

```Python
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice=random.sample(list,5)
print(slice)

[5, 3, 10, 1, 6]
```

**多个字符中选取特定数量的字符组成新字符串：**

```python
import random
import string
string.join( random.sample(['a','b','c','d','e','f','g','h','i','j'], 3) ).replace(" ","")
# 'fih'
```

**洗牌：**

代码如下:
```Python
>>> import random
>>> items = [1, 2, 3, 4, 5, 6]
>>> random.shuffle(items)
>>> items
# [3, 2, 5, 6, 4, 1]
```
