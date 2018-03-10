# datetime模块

相比于time模块，datetime模块的接口则更直观、更容易调用

**datetime模块定义了下面这几个类：**

* datetime.date：表示日期的类。常用的属性有year, month, day；
* datetime.time：表示时间的类。常用的属性有hour, minute, second, microsecond；
* datetime.datetime：表示日期时间。
* datetime.timedelta：表示时间间隔，即两个时间点之间的长度。
* datetime.tzinfo：与时区有关的相关信息。（这里不详细充分讨论该类，感兴趣的童鞋可以参考python手册）

**我们需要记住的方法仅以下几个：**

1、d=datetime.datetime.now() 返回当前的datetime日期类型

```Python
d.timestamp(),d.today(), d.year,d.timetuple()等方法可以调用
```

2、 datetime.date.fromtimestamp(322222) 把一个时间戳转为datetime日期类型

3、时间运算

```python
>>> datetime.datetime.now()

datetime.datetime(2017, 10, 1, 12, 53, 11, 821218)

>>> datetime.datetime.now() + datetime.timedelta(4) #当前时间 +4天

datetime.datetime(2017, 10, 5, 12, 53, 35, 276589)

>>> datetime.datetime.now() + datetime.timedelta(hours=4) #当前时间+4小时

datetime.datetime(2017, 10, 1, 16, 53, 42, 876275)
```

4、时间替换

```python
>>> d.replace(year=2999,month=11,day=30)

datetime.date(2999, 11, 30)
```
