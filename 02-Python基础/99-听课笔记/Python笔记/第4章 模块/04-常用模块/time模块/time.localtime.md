## 1. time.localtime([secs]): 以元组方式返回本地当前时间


* time.localtime([secs])：将一个时间戳转换为当前时区的struct_time(元组形式)。secs参数未提供，则以当前时间为准。


**时间戳————>元组形式**


```python
import time
print(time.localtime())

#输出
time.struct_time(tm_year=2018, tm_mon=3, tm_mday=11, tm_hour=9, tm_min=52, tm_sec=51, tm_wday=6, tm_yday=70, tm_isdst=0)
```
