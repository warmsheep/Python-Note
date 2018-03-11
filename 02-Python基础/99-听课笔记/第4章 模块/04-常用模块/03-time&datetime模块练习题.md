# 练习

假设你获取了用户输入的日期和时间

如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：


```python
import re                                              
from datetime import datetime, timezone, timedelta     

def to_timestamps(dt_str, tz_str):                                                                  
    dt_str = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')    #用datetime.strptime()将字符串转化为datetime类型        
    tz_str = re.match(r'UTC([+-]\d+):00',tz_str).group(1)      #暂时没看懂正则这里                                    
    dt = dt_str.replace(tzinfo=timezone(timedelta(hours=int(tz_str))))  #将datetime加上UTC=tz_str

    return dt.timestamp()   #将datetime转换为时间戳
```            
