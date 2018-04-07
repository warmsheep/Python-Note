## shutil.copymode(src, dst)

仅拷贝权限。内容、组、用户均不变

**目标文件必须存在**


```Python
import shutil

shutil.copymode('f1.log', 'f2.log') #目标文件必须存在
```
