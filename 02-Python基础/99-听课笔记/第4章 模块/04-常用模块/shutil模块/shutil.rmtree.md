## shutil.rmtree(path[, ignore_errors[, onerror]])


递归的去删除文件,注意用相对路径时的查找方法


**. 当前目录**

**.. 父级目录**


```Python
import shutil

shutil.rmtree('folder1')

shutil.rmtree('../test')
```
