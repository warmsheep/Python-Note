# time模块

在平常的代码中，我们常常需要与时间打交道。在Python中，与时间处理有关的模块就包括：time，datetime,calendar(很少用，不讲)，下面分别来介绍。

在开始之前，首先要说明几点：

**一、在Python中，通常有这几种方式来表示时间：**

1、时间戳

2、格式化的时间字符串

3、元组（struct_time）共九个元素。由于Python的time模块实现主要调用C库，所以各个平台可能有所不同。

**二、几个定义**

**UTC**（Coordinated Universal Time，世界协调时）亦即格林威治天文时间，世界标准时间。在中国为UTC+8。DST（Daylight Saving Time）即夏令时。

**时间戳**（timestamp）的方式：通常来说，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量。我们运行“type(time.time())”，返回的是float类型。

**元组**（struct_time）方式：struct_time元组共有9个元素，返回struct_time的函数主要有gmtime()，localtime()，strptime()。下面列出这种方式元组中的几个元素：


| 索引（Index）| 属性（Attribute）| 值（Values）|
|:--|:--|:--|
|0 | tm_year（年）| 比如2011|
|1 |tm_mon（月）|1 - 12|
|2 |tm_mday（日）|1 - 31|
|3 |tm_hour（时）|0 - 23|
|4 |tm_min（分）|0 - 59|
|5 |tm_sec（秒）|0 - 61|
|6 |tm_wday（weekday|0 - 6（0表示周日）|
|7 |tm_yday（一年中的第几天）|1 - 366|
|8 |tm_isdst（是否是夏令时）|  默认为-1|



## time模块的方法

**1. time.localtime([secs]): 以元组方式返回本地当前时间**
* time.localtime([secs])：将一个时间戳转换为当前时区的struct_time。secs参数未提供，则以当前时间为准。

```python
import time
print("time.localtime():",time.localtime())

#输出
time.localtime(): time.struct_time(tm_year=2018, tm_mon=3, tm_mday=11, tm_hour=9, tm_min=52, tm_sec=51, tm_wday=6, tm_yday=70, tm_isdst=0)
```


**2. time.gtime([secs]): 以元组方式返回格林威治时间**
* time.gmtime([secs])：和localtime()方法类似，gmtime()方法是将一个时间戳转换为UTC时区（0时区）的struct_time。

```python
import time
print("time.gmtime():",time.gmtime())

#输出
time.gmtime(): time.struct_time(tm_year=2018, tm_mon=3, tm_mday=11, tm_hour=1, tm_min=52, tm_sec=51, tm_wday=6, tm_yday=70, tm_isdst=0)
```


**3. time.time()：返回时间戳函数**
* time.time()：返回当前时间的时间戳。

```python
import time
print("time.time():",time.time())

#输出
time.time(): 1520733171.591093
```


**4. time.mktime(): 将元组时间转换为时间戳**
* time.mktime(t)：将一个struct_time转化为时间戳。

```python
import time
print("time.mktime(t):",time.mktime(time.localtime()))

#输出
time.mktime(t): 1520734393.0
```


**5. time.asctime(): 元组格式时间转换为字符串格式时间**

* time.asctime([t])：把一个表示时间的元组或者struct_time表示为这种形式：'Sun Oct 1 12:04:38 2017'。
* 如果没有参数，将会将time.localtime()作为参数传入。

```python
print("time.asctime():",time.asctime())

time.asctime(): Sun Mar 11 10:13:15 2018
```


**6. time.ctime(): 时间戳转换成字符串格式时间**

* time.ctime([secs])：把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。如果参数未给或者为None的时候，将会默认time.time()为参数。它的作用相当于time.asctime(time.localtime(secs))。

```python
print(time.ctime())

Sun Mar 11 10:26:06 2018
```


**7. time.strftime(): 将元组时间转换为字符串格式时间**

* time.strftime(format[, t])：把一个代表时间的元组或者struct_time（如由time.localtime()和time.gmtime()返回）转化为格式化的时间字符串。
* 如果t未指定，将传入time.localtime()。

```python
>>> x = time.localtime()
>>> time.strftime('%Y-%m-%d %H:%M:%S',x)
'2017-05-08 16:57:38'
```


**8. time.strptime(): 将字符串格式时间转换为元组格式时间**

* time.strptime(string[, format])：把一个格式化时间字符串转化为struct_time。实际上它和strftime()是逆操作。

```python
time.strptime('2017-10-3 17:54',"%Y-%m-%d %H:%M")
#输出
time.struct_time(tm_year=2017, tm_mon=10, tm_mday=3, tm_hour=17, tm_min=54, tm_sec=0, tm_wday=1, tm_yday=276, tm_isdst=-1)
```

**9. time.sleep(secs): 线程推迟运行**

* time.sleep(secs)：线程推迟指定的时间运行。单位为秒。



## 字符串转时间格式对应表

| Format | Meaning | Notes |
|:--|:--|:--|
|%a	|本地简化星期的简称|-|
|%A	|本地完整星期名称|-|
|%b	|本地简化月份名称|-|
|%B	|本地完整月份名称|-|
|%c	|本地相应的日期和时间表示|-|
|%d	|一个月中的第几天（01 - 31）|-|
|%H	|一天中的第几个小时（24小时制，00 - 23）|-|
|%I	|第几个小时（12小时制，01 - 12）|-|
|%j	|一年中的第几天（001 - 366）|-|
|%m	|月份（01 - 12）|-|
|%M	|分钟数（00 - 59）|-|
|%p	|本地am或者pm的相应符 |	(1)|
|%S	|秒（01 - 61） |	(2)|
|%U	|一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之前的所有天数都放在第0周。 |	(3)|
|%w	|一个星期中的第几天（0 - 6，0是星期天）|-|
|%W	|和%U基本相同，不同的是%W以星期一为一个星期的开始|	(3)|
|%x	|本地相应日期  |-|
|%X	|本地相应时间 |-|
|%y	|去掉世纪的年份（00 - 99）|-|
|%Y	|完整的年份|-|
|%z	|时区的名字（如果不存在为空字符）|-|
|%%	|‘%’字符| -|

最后为了容易记住转换关系，看下图

![转换关系](..\..\代码案例文稿\转换关系.png)

![转换关系](..\..\代码案例文稿\转换关系1.png)
