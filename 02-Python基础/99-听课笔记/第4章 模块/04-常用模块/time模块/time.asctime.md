## 5. time.asctime(): 元组格式时间转换为字符串格式时间

* **time.asctime([t])**：把一个表示时间的元组或者struct_time表示为字符串形式：'Sun Oct 1 12:04:38 2017'。


* 如果没有参数，将会将time.localtime()作为参数传入。


```python
print(time.asctime())

Sun Mar 11 10:13:15 2018
```
