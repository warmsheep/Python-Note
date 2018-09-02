## Basic subclasses - Adam and Eve
### 题目level
* 8kyu

### 题目描述

根据亚伯拉罕宗教的创世神话，亚当和夏娃是第一批徘徊于地球的人类。

你必须做上帝的工作。 创建方法必须返回包含对象的长度为2的数组（表示Adam和Eve）。 数组中的第一个对象应该是类Man的一个实例。 第二个应该是女性班的一个实例。 两个对象都必须是Human的子类。 你的工作是实施人类，男人和女人课程。

### 题目代码
* 我的代码

```python
def God():
    return [Man(),Woman()]
class Human:
    pass
class Woman(Human):
    pass

class Man(Human):
    pass
```

### 题目反思
* 本题就是基础的类和对象的用法
* 类是一系列属性和方法的综合
* 对象是类的实例
