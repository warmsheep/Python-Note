# datetime模块

相比于time模块，datetime模块的接口则更直观、更容易调用

**datetime模块定义了下面这几个类：**

* datetime.date：表示日期的类。常用的属性有year, month, day；
* datetime.time：表示时间的类。常用的属性有hour, minute, second, microsecond；
* datetime.datetime：表示日期时间。
* datetime.timedelta：表示时间间隔，即两个时间点之间的长度。
* datetime.tzinfo：与时区有关的相关信息。（这里不详细充分讨论该类，感兴趣的童鞋可以参考python手册）


**我们需要记住的方法仅以下几个：**

**1. datetime.datetime.now(): 返回当前时间**
* d=datetime.datetime.now() 返回当前的datetime日期类型**
* d.timestamp(),d.today(),d.year,d.timetuple()等方法可以调用

```Python
import datetime
s=datetime.datetime.now()
print(s)

2018-03-11 11:20:50.631376
```


**2. datetime.date.fromtimestamp(): 时间戳转换成日期**
* datetime.date.fromtimestamp(322222) 把一个时间戳转为datetime日期类型

```Python
>>> datetime.date.fromtimestamp(1178766678)
datetime.date(2007, 5, 10)

2007-05-10
```


**3. datetime.timedelta()：当前时间运算**
* 时间运算

* 当前时间+3天

```python
>>> datetime.datetime.now() + datetime.timedelta(3) #当前时间 +4天

datetime.datetime(2017, 10, 5, 12, 53, 35, 276589)
```


* 当前时间+3小时

```python
>>> datetime.datetime.now() + datetime.timedelta(hours=3) #当前时间+4小时

datetime.datetime(2017, 10, 1, 16, 53, 42, 876275)
```

* 当前时间+30分钟

```python
>>> datetime.datetime.now() + datetime.timedelta(minutes=30) #当前时间+4小时

datetime.datetime(2017, 10, 1, 16, 53, 42, 876275)
```

**4. .replace： 时间替换**

```python
>>> d.replace(year=2999,month=11,day=30)

datetime.date(2999, 11, 30)
```

**5. datetime.datetime(): 获取指定日期和时间**
要指定某个日期和时间，我们直接用参数构造一个datetime：

```python
>>> from datetime import datetime
>>> dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
>>> print(dt)
2015-04-19 12:20:00
```

**6. datetime.datetime.timestamp(): 将字符串转换为时间戳**






**6. datetime.tzinfo()：本地时间转换为UTC时间**

本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。

一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：

```Python
>>> from datetime import datetime, timedelta, timezone
>>> tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
>>> now = datetime.now()
>>> now
datetime.datetime(2015, 5, 18, 17, 2, 10, 871012)
>>> dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
>>> dt
datetime.datetime(2015, 5, 18, 17, 2, 10, 871012, tzinfo=datetime.timezone(datetime.timedelta(0, 28800)))
```

如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区。


**7. datetime.utcnow()：时区转换**

```Python
# 拿到UTC时间，并强制设置时区为UTC+0:00:
>>> utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
>>> print(utc_dt)
2015-05-18 09:05:12.377316+00:00
# astimezone()将转换时区为北京时间:
>>> bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
>>> print(bj_dt)
2015-05-18 17:05:12.377316+08:00
# astimezone()将转换时区为东京时间:
>>> tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
>>> print(tokyo_dt)
2015-05-18 18:05:12.377316+09:00
# astimezone()将bj_dt转换时区为东京时间:
>>> tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
>>> print(tokyo_dt2)
2015-05-18 18:05:12.377316+09:00
```

时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。

利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。

**注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。**


## 转换关系

![转换关系](..\..\代码案例文稿\datetime转换.png)

## 小结

datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。

如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。
