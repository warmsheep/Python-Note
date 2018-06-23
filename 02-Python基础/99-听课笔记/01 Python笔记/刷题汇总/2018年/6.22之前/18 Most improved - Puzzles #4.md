## Most improved - Puzzles #4

### 题目level
* 6kyu

### 题目描述
* 在某个科目或某个课程中进行评分时，评分最高的是最重要的，但哪些方面的评分最高？作为一名计算机科学教师，您希望创建一个计算最优化学生的函数，并将它们排列在列表中。

**任务**
* 你的任务是强制calculateImproved函数返回一个按百分比最大改进排序的数组。

**输入**
* 您将收到的输入将是一组学生，学生将是一个包含名称和标记数组的对象（按照成绩排列），标记将不超过100，但是如果测试的学生可以标记为空没有尝试（把它当作0）
学生对象示例：
```python
{name:'Henry, Johns','marks':[25,50]}
{name:'Alex, Bug','marks':[None,100]}
{name:'Blach, Joe','marks':[0,100]}
{name:'Kjax, Cue','marks':[0,None]}
{name:'Cod with','marks':[90,None]}
```

**产量**
* 预期的输出将是一个类似于学生对象的对象数组，其中包含名称和总计提高百分比，用于计算总体提高百分比。输出数组必须按大多数改进进行排序（舍入计算的改进）如果改进中存在联系，则按名称排序（大写在小写之前）。

返回对象示例：
```python
{name:'Henry, Johns',"improvement":100}
{name:'Alex, Bug',"improvement":0}
{name:'Blach, Joe',"improvement":0}
{name:'Kjax, Cue',"improvement":0}
{name:'Cod with',"improvement":-100.0}
```

**预装**
* Student类已经预装了接受两个参数的构造函数名称和标记，这些参数应该是数字数组。


### 题目思路
* 1.先将所有情况讨论(for i in studnets)，新增improvement键值，并移除marks键值对:
  * 1.1 首项不为0或None，尾项不为None
  * 1.2 首项不为0或None，尾项为None
  * 1.3 首项为0或None
* 2.针对新列表进行排序，排序要求为先按照分数降序，再按照姓名升序。
* 注意:在python3.6中对字典新增的值一般都显示在最后一对k-v中，但是在python2.7中新增的值不一定是显示在最后一对k-v中，所以这点记住，对本体题来说显示的时候其实这个不是很重要，但是对于有的题目可能就需要注意一下。

### 题目代码
* 我的代码
```python
from __future__ import division
def calculate_improved(students):
    for i in students:
        if i["marks"][0]:
            if not i["marks"][-1] ==None:
                i["improvement"]=round(float(i["marks"][-1]/i["marks"][0]-1)*100)
            else:
                i["improvement"]=-100.0
        else:
            i["improvement"] = 0
        i.pop("marks")
    return sorted(students,key=lambda x:(-x.get("improvement"),x["name"]))
```

* 优秀代码
```python
def calculate_improved(students):
    students = ({
        "name"       : s["name"],
        "improvement": round(
            100.0 * (s["marks"][-1] or 0) / (s["marks"][0] or 0) - 100.0)
            if s["marks"][0] else 0
    } for s in students)
    return sorted(students, key=lambda s: (-s["improvement"], s["name"]))
```
### 题目反思
##### 我的代码反思
* 1.个人觉得这个题的描述太过省略了，本例题中的总结中我把题目描述所有的情况都写进去了，但是kata的描述只有第一个，我需要每次试错才能知道情况，所以针对这个题目我觉得题目描述太不明朗，建议大家做个题先来看看我的描述，少走点弯路。

* 2.另外一个就是版本问题，题目中只能用python2.7，而我一直用的python3.6版本，版本不同会导致除法运算的结果不同:

  * 除法运算，关于这两个除法运算的区别如下:

    python2.7
    ```python
    >>> 1/3
    0
    >>> 28/14
    2
    >>> 28/15
    1
    ```
    python3.6
    ```python
    >>> 1/3
    0.3333333333333333
    >>> 28/14
    2.0
    >>> 28/15
    1.8666666666666667
    ```
    解决方法一:引用模块

    ```python
    from __future__ import division
    ```

    ```python
    >>> from __future__ import division
    >>> 1/3
    0.3333333333333333
    ```
    解决方法二:将数字float后再进行除法运算
    ```python
    >>> float(2)/float(4)
    0.5
    >>> float(2)/float(2220)
    0.0009009009009009009
    ```

* 3.针对一个列表中如何进行多条件排序，这个会在新学知识点有所总结。

##### 优秀代码总结
**思路**
看了一下排序和我的代码没啥区别，只是计算improvement的差别，其思路为:

* 1.1 计算原始"improvement"
```
Inc=(100*(最新的值/起始值)-100) if 起始值有意义(排除了None和O的情况) else 0
```
* 1.2 排除可能存在的错误:

  * 最新的值可能出现None导致计算类型出错，所以避免这种情况的出现，使用or来解决这种错误(最新值 or 0)，同样也对起始值这样避免问题。
```
Inc=(100*(最新的值 or 0）/(起始值 or 0)-100) if 起始值有意义 else 0
```
* 1.4 round(Inc) 对增幅值保留一位小数

```
针对优秀代码有个小小可以改正的点:
if s["marks"][0]已经排除了为0和None的情况，
所以它作为分母始终是有意义的，不需要在写成(s["marks"][0] or 0)，
直接写成 s["marks"][0]
```
**改写后的代码如下:**

```python
def calculate_improved(students):
    students = ({
        "name": s["name"],
        "improvement": round(
            100.0 * (s["marks"][-1] or 0) / s["marks"][0] - 100.0)
            if s["marks"][0] else 0
    } for s in students)
    return sorted(students, key=lambda s: (-s["improvement"], s["name"]))
```




##### 新学知识点

* 1.针对2.7版本的如果需要实现3.6的除法效果，添加模块最省事儿

```python
from __future__ import division
```
**排序**
* 2.1 单条件排序
```
方法有两种，
a. 笔记中的operator模块下的getteritem,这里就不详细说了，
b. lambda函数
```
```python
#针对固定位置的值，升序
sorted(iterable,key=lambda x:x[index])
#针对某个键的值，升序
sorted(iterable,key=lambda x:x[key])
```

```python
s=[ ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),]
sorted(s, key=lambda student: student[2])
#输出结果
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

```python
s_dic=[{"name":"alex","age":18},{"name":"peqi","age":20},{"name":"egon","age":28}]
sorted(s_dic,key=lambda x:x.get("age"))
#输出结果
[{'name': 'alex', 'age': 18}, {'name': 'peqi', 'age': 20}, {'name': 'egon', 'age': 28}]
```

* 2.2 多条件排序

```python
#针对固定位置的值，升序
sorted(iterable,key=lambda x:(x[index1],x[index2]))
#针对某个键的值，依次按照升序排列
sorted(iterable,key=lambda x:(x[key1],x[key2]...))
```
* 先对年龄升序，如果年龄相同对名字升序排列。

```python
s_dic=[{"name":"alex","age":18},{"name":"peqi","age":20},{"name":"egon","age":20}]
sorted(s_dic,key=lambda x:(x["age"],x["name"]))
#输出结果
[{'name': 'alex', 'age': 18}, {'name': 'egon', 'age': 20}, {'name': 'peqi', 'age': 20}]
```

* **问题1:** 如果我要对一个升序一个降序排列呢？比如先对针对上个例子年龄降序排列，年龄相同名字再升序排列？

* **解决1:** 直接用多条件排序都是升序排列，所以针对年龄来说降序排列也就是对年龄的负数升序排列，转换过来就ok了，在x["age"]前面加个符号:

```python
s_dic=[{"name":"alex","age":18},{"name":"peqi","age":20},{"name":"egon","age":20}]
sorted(s_dic,key=lambda x:(-x["age"],x["name"]))
#输出结果
[{'name': 'egon', 'age': 20}, {'name': 'peqi', 'age': 20}, {'name': 'alex', 'age': 18}]
```

* **问题2:** 如果我要对上例题中的年龄升序排列，但是名字降序排列呢？

* **解决2:** 针对这个问题，将问题1反转过来，就OK了

```python
s_dic=[{"name":"alex","age":18},{"name":"peqi","age":20},{"name":"egon","age":20}]
sorted(s_dic,key=lambda x:(-x["age"],x["name"]),reverse=True)
#输出结果
[{'name': 'alex', 'age': 18}, {'name': 'peqi', 'age': 20}, {'name': 'egon', 'age': 20}]
```
**多类型书写**
* 针对可能出现的类型的错误，可以用or来解决这种问题，这样可以不用一直用if来解决，一个括号和or就能管事儿。
