# yield总结


### 包含yield的函数

假如你看到某个函数包含了yield，这意味着这个函数已经是一个Generator，它的执行会和其他普通的函数有很多不同。比如下面的简单的函数：


### yiled赋值

Python2.5以前，yield是一个语句，但在2.5中，yield是一个表达式(Expression)，比如：

```python
m = yield 5
```

表达式(yield 5)的返回值将赋值给m，所以，认为 m = 5 是错误的。那么如何获取(yield 5)的返回值呢？需要用到后面要介绍的send(msg)方法。

本例子中的baozi = yield 的意义一样，将yield返回值赋值给baozi

### send(msg)

其实next()和send()在一定意义上作用是相似的，区别是send()可以传递yield表达式的值进去，而next()不 能传递特定的值，只能传递None进去。因此，我们可以看做
c.next() 和 c.send(None) 作用是一样的。

```python
c.send(i) #(baozi=yield)表达式被赋予了'i'
```

**注意**

需要提醒的是，第一次调用时，请使用next()语句或是send(None)，不能使用send发送一个非None的值，否则会出错的，因为没有yield语句来接收这个值。


### yield应用

**还可通过yield实现在单线程的情况下实现并发运算的效果**

```python
__author__ = 'Alex Li'

import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield

       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i)
        c2.send(i)

producer("alex")
#通过生成器实现协程并行运算　
```
