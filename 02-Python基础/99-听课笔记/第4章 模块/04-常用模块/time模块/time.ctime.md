## 6. time.ctime(): 时间戳转换成字符串格式时间


* **time.ctime([secs])**：把一个时间戳（按秒计算的浮点数）转化为time.asctime() **字符串** 的形式。


* 如果参数未给或者为None的时候，将会默认time.time()为参数。它的作用相当于time.asctime(time.localtime(secs))。


```python
print(time.ctime())

Sun Mar 11 10:26:06 2018
```
