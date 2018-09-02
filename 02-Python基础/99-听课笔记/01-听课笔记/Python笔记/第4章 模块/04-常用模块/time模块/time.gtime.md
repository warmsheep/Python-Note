## 2. time.gtime([secs]): 以元组方式返回格林威治时间

* time.gmtime([secs])：和localtime()方法类似，gmtime()方法是将一个时间戳转换为UTC时区（0时区）的struct_time（元组形式）。


**时间戳————>元组（UTC=0）**


```python
import time
print(time.gmtime())

#输出
 time.struct_time(tm_year=2018, tm_mon=3, tm_mday=11, tm_hour=1, tm_min=52, tm_sec=51, tm_wday=6, tm_yday=70, tm_isdst=0)
```
